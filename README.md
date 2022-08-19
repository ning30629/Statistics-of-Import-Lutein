# 國內進口葉黃素產地來源統計

### 簡介

> 現代人不論是工作或是休閒娛樂，對於電子產品的依賴越來越大，眼睛的負擔也是日益加重。因此，葉黃素成為許多人每日必須補充的保健食品。
> 此專案的目的為統計進口至國內葉黃素的產地來源(資料來源為食品衛生藥物管理署)，作為挑選保健食品時的選擇依據。

#### 專案內各程式碼功能介紹:

- FDA_lutein.py
  - 使用 selenium 自動爬取目標網站每一頁的資料
  - 在所有抓取下來的資料中，取出所需要的目標資料
  - 將目標資料的列表處理成可以轉換成 csv 的格式
  - 將結果存成 csv 檔
- lutein_csv_into_SQLite
  - 將 csv 檔資料來源匯入 SQLite 資料庫
- get_fig
  - 將 csv 資料視覺化，輸出長條圖表

#### 執行此專案將獲得的資料為以下:

- 來源資料 csv 檔
- 資料統計圖表
- SQLite 資料庫

## 執行專案前的準備

- python 3
- virtualenv
- 套件: 請參考 requirements.txt
- SQLite
- DB Browser (SQLite)
- 安裝中文字體，供輸出成長條圖時使用

#### 安裝中文字體步驟說明

> 此專案使用可以開源及商用的免費字體-台北黑體  
> [下載連結請點此](https://sites.google.com/view/jtfoundry/)

```
1. 下載字體後，將字體放入以下資料夾路徑
   D:\專案資料夾\Lib\site-packages\matplotlib\mpl-data\fonts\ttf
2. 到以下資料夾路徑刪除快取檔案(fontList.json)並重新 import matplotlib
   C:\Users\電腦名稱\.matplotlib
3. 完成，依程式碼執行即可獲得中文化長條圖表
```

## 執行程式碼的順序

1. 請先執行 FDA_lutein.py，以取得 csv 檔資料
2. 其餘程式碼可以依個人需求決定執行順序
