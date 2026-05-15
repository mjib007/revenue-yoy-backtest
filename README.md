# 📊 月營收 YoY 回測分析

![Profile views](https://komarev.com/ghpvc/?username=mjib007&label=Profile%20views&color=4c8eda&style=flat)
[![Stars](https://img.shields.io/github/stars/mjib007/revenue-yoy-backtest?style=flat&color=yellow)](https://github.com/mjib007/revenue-yoy-backtest/stargazers)
[![Forks](https://img.shields.io/github/forks/mjib007/revenue-yoy-backtest?style=flat&color=blue)](https://github.com/mjib007/revenue-yoy-backtest/network/members)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Platform](https://img.shields.io/badge/Platform-Google%20Colab-orange)
![Data](https://img.shields.io/badge/Data-FinMind%20%7C%20yfinance-green)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
![Status](https://img.shields.io/badge/status-active-success)

> **核心問題：當某股票月營收年增率（YoY）超過門檻時，買入持有 N 天的勝率有多少？**

本專案提供三個版本的 Jupyter Notebook，適合不同程度的使用者。

---

## 🚀 快速開始（點一下，直接執行）

**不需要安裝任何軟體，不需要下載任何檔案。**
點下方按鈕，瀏覽器直接開啟，就可以執行。

| 版本 | 說明 | 開啟 |
|------|------|------|
| 📖 教材版 | 有完整步驟說明，適合初次學習 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mjib007/revenue-yoy-backtest/blob/main/01_月營收YoY回測_教材版.ipynb) |
| ⚡ 單一Cell版 | 改好參數直接跑，適合快速使用 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mjib007/revenue-yoy-backtest/blob/main/02_月營收YoY回測_單Cell版.ipynb) |
| 💬 指令輸入版 | 用自然語言下指令，適合 Vibe Coding | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mjib007/revenue-yoy-backtest/blob/main/03_月營收YoY回測_指令輸入版.ipynb) |

### ❓ Open in Colab 是什麼？

點擊按鈕後，程式碼會在**你自己的 Google 帳號**下開啟並執行：
- 程式在你自己的 Colab 環境跑，不影響任何人
- 完全免費，不需要信用卡
- 關掉視窗後不會留下任何紀錄

如果你想**儲存執行結果或修改內容**，點上方選單「**檔案**」→「**在雲端硬碟中儲存副本**」，存到自己的 Google 雲端即可。不存的話，下次點連結又是原始乾淨的版本。

---

## 📋 三個版本的差異

### 📖 教材版（適合第一次使用）
- 每個步驟都有說明，讀得懂每一行在做什麼
- Step 1 安裝套件 → Step 7 多時間窗口比較
- 適合想搞懂程式邏輯的學習者

### ⚡ 單一 Cell 版（適合快速使用）
- 只有一個大 Cell，改參數後直接全部執行
- 修改區塊清楚標示，不需要理解程式邏輯
- 適合只想跑結果、不想研究程式的使用者

### 💬 指令輸入版（適合 Vibe Coding）
- 執行後出現輸入框，用自然語言下指令
- 例如輸入：`2330.TW 月營收 20% 持有20天`
- 完全不需要修改任何程式碼
- 想客製化功能？把程式碼貼給 Claude / ChatGPT，說「幫我加上 XX 功能」

---

## 🔧 可調整的參數

| 參數 | 說明 | 預設值 |
|------|------|--------|
| `STOCK_ID` | 股票代號（不含後綴）| `2330` |
| `MARKET` | 上市填 `TW`，上櫃填 `TWO` | `TW` |
| `YOY_THRESHOLD` | YoY 觸發門檻（%） | `20` |
| `HOLD_DAYS` | 買入後持有天數 | `20` |
| `START_DATE` | 回測起始日期 | `2015-01-01` |
| `FINMIND_TOKEN` | FinMind Token（可留空，有填可抓更多資料）| 空白 |

---

## 📦 資料來源

- **月營收資料**：[FinMind](https://finmindtrade.com/)（台灣開源金融資料平台，免費使用）
- **股價資料**：[yfinance](https://pypi.org/project/yfinance/)

---

## 💬 Vibe Coding 提示語

不需要懂 Python！把程式碼複製，貼給 Claude 或 ChatGPT，說：

```
我有一段月營收 YoY 回測的程式碼（如下），請幫我改成可以同時回測多支股票的版本。
[貼上程式碼]
```

其他改法範例：
- 「加上停損條件，跌超過 5% 就出場」
- 「把圖表改成英文標籤」
- 「改成可以輸入多個 YoY 門檻比較」

---

## ⚠️ 免責聲明

本專案僅供學術研究與程式教學用途，所有回測結果均基於歷史資料，不代表未來績效，不構成任何投資建議。投資有風險，請自行評估。

---

## 👨‍🏫 關於作者

本專案由**小龍蝦 AI 課程**提供，課程收入全數捐入基金會。
