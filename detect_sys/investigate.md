# 調査
### 時間データを確認

<div style="display:flex; gap:24px;">

<table style = "outline:none;">
    <tr>
        <td> 
            <table>
            <div>DATA11_ﾃｰﾌﾞﾙ位置決め 下降</div>
            <tr><th>TIME</th><th>Value (ms)</th></tr>
            <tr><td>2026/2/25 15:42</td><td>1489569</td></tr>
            <tr><td>2026/2/25 15:42</td><td>1500710</td></tr>
            <tr><td>2026/2/25 15:43</td><td>1496740</td></tr>
            <tr><td>2026/2/25 15:43</td><td>1493900</td></tr>
            <tr><td>2026/2/25 15:44</td><td>1487810</td></tr>
            <tr><td>2026/2/25 15:44</td><td>1486069</td></tr>
            <tr><td>2026/2/25 15:45</td><td>1468520</td></tr>
            <tr><td>2026/2/25 15:45</td><td>1469171</td></tr>
            <tr><td>2026/2/25 15:46</td><td>1465450</td></tr>
            <tr><td>2026/2/25 15:47</td><td>1468971</td></tr>
            <tr><td>2026/2/25 15:47</td><td>1472550</td></tr>
            <tr><td>2026/2/25 15:48</td><td>1465901</td></tr>
            <tr><td>2026/2/25 15:48</td><td>1474801</td></tr>
            <tr><td>2026/2/25 15:48</td><td>1483740</td></tr>
            <tr><td>2026/2/25 15:49</td><td>1497970</td></tr>
            <tr><td>2026/2/25 15:49</td><td>1507220</td></tr>
            <tr><td>2026/2/25 15:50</td><td>1517350</td></tr>
            <tr><td>2026/2/25 15:50</td><td>1517670</td></tr>
            <tr><td>2026/2/25 15:50</td><td>1518330</td></tr>
            <tr><td>2026/2/25 15:51</td><td>1519049</td></tr>
            </table>
        </td>
        <td>
            <table>
            <div>DATA01_ｴﾊﾞ位置決め部押え1 後退</div>
            <tr><th>TIME</th><th>Value (ms)</th></tr>
            <tr><td>2026/2/25 15:42</td><td>220</td></tr>
            <tr><td>2026/2/25 15:43</td><td>219</td></tr>
            <tr><td>2026/2/25 15:43</td><td>220</td></tr>
            <tr><td>2026/2/25 15:44</td><td>211</td></tr>
            <tr><td>2026/2/25 15:45</td><td>221</td></tr>
            <tr><td>2026/2/25 15:45</td><td>209</td></tr>
            <tr><td>2026/2/25 15:46</td><td>209</td></tr>
            <tr><td>2026/2/25 15:46</td><td>219</td></tr>
            <tr><td>2026/2/25 15:47</td><td>209</td></tr>
            <tr><td>2026/2/25 15:47</td><td>220</td></tr>
            <tr><td>2026/2/25 15:48</td><td>210</td></tr>
            <tr><td>2026/2/25 15:48</td><td>210</td></tr>
            <tr><td>2026/2/25 15:48</td><td>220</td></tr>
            <tr><td>2026/2/25 15:49</td><td>219</td></tr>
            <tr><td>2026/2/25 15:49</td><td>219</td></tr>
            <tr><td>2026/2/25 15:50</td><td>209</td></tr>
            <tr><td>2026/2/25 15:50</td><td>221</td></tr>
            <tr><td>2026/2/25 15:51</td><td>219</td></tr>
            <tr><td>2026/2/25 15:51</td><td>209</td></tr>
            <tr><td>2026/2/25 15:52</td><td>220</td></tr>
            </table>
        </td>
    </tr>
</table>
</div>

###　グラフで確認
![全体画像_DATA11](./img/DATA11_plot.png)

![全体画像_DATA01](./img/DATA02_plot.png)


### 生データをグラフで確認
<div>DATA11_ﾃｰﾌﾞﾙ位置決め 下降</div>
<img src="./img/DATA11_NG_20260225.png" width = 49.5%>
<img src="./img/DATA11_NG_ZOOM_20260225.png" width = 49.5%>
⇒下降の指示(0, 1)と、下降端の指示(0, 1)がなんとなくイメージと乖離する
<div>全体がずれているわけでもなく、うまく重なっているところもある</div>
<img src="./img/DATA11_OK_20260225.png" width = 49.5%>

<br><br>
<div>DATA02_ｴﾊﾞ位置決め部押え1 前進</div>
<img src="./img/DATA2_OK_20260225.png" width = 49.5%>
<img src="./img/DATA2_OK_ZOOM_20260225.png" width = 49.5%>
⇒イメージ通り。前進が入って、前進端がONしたと同時に、前進の自己保持が切れる


## 書き方参考
>[Markdown記法一覧](https://qiita.com/oreo/items/82183bfbaac69971917f "Markdown記法一覧")