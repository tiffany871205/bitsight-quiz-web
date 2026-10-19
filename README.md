# Bitsight Learning Lab｜題庫搜尋與模擬考試

靜態網站，無須安裝 Node 套件或後端，支援 GitHub Pages。題庫取自上一層的 `Bitsight_主管考試與實務題庫_Notion版.md`，共 400 題。

## 本機預覽

在 Mac 終端機執行：

```bash
cd '/Users/tiffanytai/Desktop/未命名檔案夾/bitsight-knowledge/quiz-web'
python3 -m http.server 8080
```

瀏覽器開啟 `http://localhost:8080`。請勿直接雙擊 `index.html` 以 `file://` 開啟，否則瀏覽器可能阻擋 JSON 載入。

## 功能

- **題庫搜尋**：400 題全文搜尋（包含答案、解析）、分類與來源篩選、展開答案、分批顯示。
- **模擬考試**：分類與題數、隨機四選一、上一題／下一題、交卷計分、逐題解析、錯題重練。
- **瀏覽器記錄**：錯題與最近成績儲存在該瀏覽器 `localStorage`；更換裝置或清除網站資料後不會同步。
- **RWD**：適用桌面及手機。

## 題目品質與來源

`questions.json` 由同資料夾的 `../Bitsight_主管考試與實務題庫_Notion版.md` 產生。**題目、正解及既有解析均來自原始題庫**；其他三個干擾選項由同分類其他題目的答案自動抽取，可能存在選項較容易排除的情況，**並非 Bitsight 官方題庫**。作答正確與否以來源題庫原答案為準；少數原題只有答案，解析會提示參照主知識庫。

若題庫更新，請同步重新產生 `questions.json`，避免網站與 Markdown 不一致。

## 部署到 GitHub Pages

將 `quiz-web` 內的 `index.html`、`styles.css`、`app.js`、`questions.json` 放在 GitHub repository 根目錄，推送到 GitHub。到 `Settings → Pages → Build and deployment` 選擇 `Deploy from a branch`、`main`、`/(root)`，儲存後等待部署。也可以將整個資料夾放在 repo 子路徑並從對應位置部署。

## 隱私

網站無需登入、不會向外部伺服器提交作答紀錄，僅在本機瀏覽器儲存錯題與成績。未加入分析追蹤程式。
