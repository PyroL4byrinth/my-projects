#############################################################
#
# モデル検証用プログラム
#
#
#
#
#
#
#
#
#
#
#
#
#
#############################################################

## ワークスペース初期化
rm(list = ls()) # 現環境のオブジェクトをすべて解放（削除）する
# gc():garbage collection:未使用のメモリを回収
gc(); gc()

## パッケージ読み込み & インストール
Force <- FALSE
pkgs <- c("dplyr", "data.table", "ggplot2", "plotly","caret","np")
for (pkg in pkgs){
  # 読み込みに失敗したらインストールしてから再読み込み
  # require()：パッケージの読み込み時、失敗した場合FLASEを返して続行する関数
  # library()：パッケージの読み込み時、失敗した場合エラーで停止する関数
  # character.only = TURE:パッケージ名を文字列で渡す（デフォルトは、シンボル）
  if(Force || !require(pkg, character.only = TRUE)){
    install.packages(pkg)
    library(pkg, character.only = TRUE)
  }
}

## 自作関数の読み出し
funcs <- c("func_fit_model.R", "func_predict_model.R")
for (func in funcs){
  source(func)
}

## データソース変数
DATA_SOURCES <- "C:/GitHub/data-stored/lin2.csv"
CATEGORY_DATA <- "./output/category_lin2.csv"
PROCESS_NUMBER <- "./source/ProcessNumber.csv"

## 説明変数(X)と目的変数(Y)
X_NAME <- "sum_equip_item_name - 熱かしめ_測定値|コイル熱かしめ温度1 - value"
Y_NAME <- "sum_equip_item_name - はんだ付_測定値|コイル端子位置座標X1 - value"
x <- 300

## CSV読み込み
df <- read.csv(DATA_SOURCES, header = TRUE, check.names = FALSE)
df_xy <- df[c(X_NAME, Y_NAME)]

## CategoryData読み込み
df_cat <- read.csv(CATEGORY_DATA, header = TRUE, check.names = FALSE, fileEncoding = "CP932")
X_CATEGORY = df_cat$type[df_cat$fullname == X_NAME]
Y_CATEGORY = df_cat$type[df_cat$fullname == Y_NAME]
XY_CATEGORY = paste0(X_CATEGORY, "_", Y_CATEGORY)

## 学習（Yは多変量もOK） 
m <- switch(XY_CATEGORY,
  "Low_Low" = fit_condfreq(df_xy[[X_NAME]],df_xy[[Y_NAME]]),
  "Low_MidInt" = fit_poisson(df_xy[[X_NAME]],df_xy[[Y_NAME]]),
  "Low_MidFloat" = fit_nonparametric(df_xy[[X_NAME]], df_xy[[Y_NAME]]),
  "Low_HighNum" = "",
  "MidInt_Low" = "",
  "MidInt_MidInt" = "",
  "MidInt_MidFloat" = "",
  "MidInt_HighNum" = "",
  "MidFloat_Low" = "",
  "MidFloat_MidInt" = "",
  "MidFloat_MidFloat" = "",
  "MidFloat_HighNum" = "",
  "HighNum_Low" = "",
  "HighNum_MidInt" = "",
  "HighNum_MidFloat" = "",
  "HighNum_HighNum" = ""
)

## 予測（Yは多変量もOK） 
res <- switch(XY_CATEGORY,
  "Low_Low" = predict_condfreq(m, x, type = "prob"),
  "Low_MidInt" = predict_poisson(m, x),
  "Low_MidFloat" = predict_nonparamestic(m, x, df_xy[[Y_NAME]]),
  "Low_HighNum" = "",
  "MidInt_Low" = "",
  "MidInt_MidInt" = "",
  "MidInt_MidFloat" = "",
  "MidInt_HighNum" = "",
  "MidFloat_Low" = "",
  "MidFloat_MidInt" = "",
  "MidFloat_MidFloat" = "",
  "MidFloat_HighNum" = "",
  "HighNum_Low" = "",
  "HighNum_MidInt" = "",
  "HighNum_MidFloat" = "",
  "HighNum_HighNum" = ""
)

# グラフ化
p <- ggplot(res, aes(x = res$y, y = res$f)) +
      geom_point() +
      geom_line()

ggplotly(p)

