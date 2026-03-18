import glob
import os
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

from pathlib import Path
import re
from datetime import datetime, timedelta
from bisect import bisect_left

# ファイル名: INPUT_M_YYYYMMDD_HHMMSS_通し番号.csv
_RE = re.compile(r"^INPUT_M_(\d{8})_(\d{6})_(\d+)\.csv$", re.IGNORECASE)

def _list_day_files(day_folder: Path):
    """1日フォルダ内のファイルを (datetime, path) のリストで返す（時刻順）"""
    items = []
    for p in day_folder.glob("INPUT_M_*.csv"):
        m = _RE.match(p.name)
        if not m:
            continue
        dt = datetime.strptime(m.group(1) + m.group(2), "%Y%m%d%H%M%S")
        items.append((dt, p))
    items.sort(key=lambda x: x[0])
    return items

def select_files(root_bak: str, start_dt: datetime, minutes: int, mode="floor"):
    """
    start_dt に近いファイルを先頭に、minutes*6本のファイルパスを返す。
    mode: 'floor' | 'nearest' | 'ceil'
    """
    root = Path(root_bak)
    n_files = minutes * 6  # 10秒/本 → 1分=6本

    # まず開始日のフォルダを読む（必要なら翌日分も後で足す）
    day0 = start_dt.strftime("%Y%m%d")
    folder0 = root / f"INPUT_M{day0}"
    if not folder0.exists():
        raise FileNotFoundError(f"日フォルダが見つからない: {folder0}")

    day_items = _list_day_files(folder0)
    if not day_items:
        raise FileNotFoundError(f"CSVが見つからない: {folder0}")

    dts = [dt for dt, _ in day_items]
    idx = bisect_left(dts, start_dt)

    # 先頭インデックスを決める
    if mode == "ceil":
        start_idx = min(idx, len(day_items) - 1)

    elif mode == "nearest":
        if idx <= 0:
            start_idx = 0
        elif idx >= len(day_items):
            start_idx = len(day_items) - 1
        else:
            prev_dt = dts[idx - 1]
            next_dt = dts[idx]
            start_idx = (idx - 1) if (start_dt - prev_dt <= next_dt - start_dt) else idx

    else:  # 'floor' 推奨：start_dt以前で最も近い
        start_idx = max(0, idx - 1) if idx > 0 else 0

    selected = [p for _, p in day_items[start_idx:start_idx + n_files]]

    # 足りなければ翌日フォルダを追加（durationが長い場合の保険）
    if len(selected) < n_files:
        day1 = (start_dt + timedelta(days=1)).strftime("%Y%m%d")
        folder1 = root / f"INPUT_M{day1}"
        if folder1.exists():
            day1_items = _list_day_files(folder1)
            remain = n_files - len(selected)
            selected.extend([p for _, p in day1_items[:remain]])

    return selected

# ====== 設定 ======
folder = r"//10.112.137.53/detect_sys/bak"   # CSVが入ってるフォルダ（例: r"C:\data\csv"）
col1 = "ﾃｰﾌﾞﾙ位置決め 下降"             # 取り出したい列1
col2 = "ﾃｰﾌﾞﾙ位置決め 下降端"             # 取り出したい列2
time_col = "TIME"          # 時刻列名
encoding = "cp932"         # 文字化けするなら "cp932" も試す
start_dt = datetime(2026, 2, 25, 10, 15, 0)  # 10:15:00
# ==================

paths = select_files(folder, start_dt, minutes=120, mode="floor")

dfs = []
for p in paths:
    df = pd.read_csv(p, encoding=encoding, header=2)
    df["__source__"] = os.path.basename(p)  # どのCSV由来か残す（不要なら消してOK）
    dfs.append(df)

# 行結合（縦結合）
all_df = pd.concat(dfs, ignore_index=True)

# 必要列だけ取り出し（存在チェックも兼ねる）
need = [time_col, col1, col2]
missing = [c for c in need if c not in all_df.columns]
if missing:
    raise KeyError(f"列が見つからない: {missing}\n存在する列: {list(all_df.columns)}")

plot_df = all_df[need].copy()

# TIMEをdatetimeに変換（失敗はNaTに）
plot_df[time_col] = pd.to_datetime(plot_df[time_col], errors="coerce")
plot_df = plot_df.dropna(subset=[time_col]).sort_values(time_col)

# 値列を数値化（文字が混ざる場合に備える）
plot_df[col1] = pd.to_numeric(plot_df[col1], errors="coerce")
plot_df[col2] = pd.to_numeric(plot_df[col2], errors="coerce")

# ====== グラフ ======
plt.figure(figsize=(12, 5))
plt.plot(plot_df[time_col], plot_df[col1], label=col1)
plt.plot(plot_df[time_col], plot_df[col2], label=col2)
plt.xlabel(time_col)
plt.ylabel("Value")
plt.title(f"{col1} & {col2} vs {time_col}")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()