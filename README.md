# 📊 月營收 YoY 回測分析

![Profile views](https://komarev.com/ghpvc/?username=mjib007&label=Profile%20views&color=4c8eda&style=flat)
[![Stars](https://img.shields.io/github/stars/mjib007/revenue-yoy-backtest?style=flat&color=yellow)](https://github.com/mjib007/revenue-yoy-backtest/stargazers)
[![Forks](https://img.shields.io/github/forks/mjib007/revenue-yoy-backtest?style=flat&color=blue)](https://github.com/mjib007/revenue-yoy-backtest/network/members)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Platform](https://img.shields.io/badge/Platform-Google%20Colab-orange)
![Data](https://img.shields.io/badge/Data-FinMind%20%7C%20yfinance-green)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
![Status](https://img.shields.io/badge/status-active-success)

> 🦞 **這是一個學習如何自己打造小龍蝦 OpenClaw AI 助理的學習教材。**
> 透過「月營收 YoY 回測」這個實際功能，帶你從零開始，一步一步理解小龍蝦的每一個工具是怎麼設計出來的。
> 學會之後，把程式碼存成 `.py` 檔案，就可以在自己的電腦上直接執行囉！

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


---

---

## 📁 檔案說明

| 檔案 | 用途 |
|------|------|
| `README.md` | 專案說明頁（你現在看的這份）|
| `01_月營收YoY回測_教材版.ipynb` | 逐步教學版，每個步驟都有說明 |
| `02_月營收YoY回測_單Cell版.ipynb` | 一格執行版，改好參數直接跑 |
| `03_月營收YoY回測_指令輸入版.ipynb` | 自然語言輸入版，適合 Vibe Coding |
| `月營收YoY回測.py` | 本機執行版，下載後在自己電腦直接跑 |

## 💻 進階：在自己的電腦上執行

學會在 Colab 使用之後，想在自己電腦跑？跟著以下步驟設定環境。

### 第一步：安裝 Anaconda

Anaconda 是一個幫你管理 Python 環境的工具，安裝完就自動包含 Python 和 Jupyter Notebook。

1. 前往 👉 https://www.anaconda.com/download
2. 選擇你的作業系統（Windows / Mac），點擊下載
3. 執行安裝檔，一路按「Next」，最後按「Install」
4. 安裝完成後，開啟「**Anaconda Navigator**」確認安裝成功

> ⏱️ 安裝約需 5–10 分鐘

---

### 第二步：下載程式碼

1. 回到這個 GitHub 頁面
2. 點右上角綠色「**Code**」按鈕
3. 選「**Download ZIP**」
4. 解壓縮到你想放的資料夾，例如桌面的 `revenue-yoy-backtest` 資料夾

---

### 第三步：開啟 Jupyter Notebook

1. 開啟「**Anaconda Navigator**」
2. 點「**Jupyter Notebook**」→「**Launch**」
3. 瀏覽器會自動開啟，找到你剛才解壓縮的資料夾
4. 點進去，選擇任一個 `.ipynb` 檔案開啟

---

### 第四步：安裝需要的套件

第一次執行時，需要安裝套件。開啟 `01_月營收YoY回測_教材版.ipynb`，執行第一個 Cell（Step 1 安裝套件），等待安裝完成即可。

> ⚠️ 只需要安裝一次，之後每次執行不需要重複安裝。

---

### 第五步（進階）：存成 .py 在終端機執行

如果你想把程式存成 `.py` 直接在終端機跑：

1. 開啟「**Anaconda Prompt**」（Windows）或「**Terminal**」（Mac）
2. 切換到你的資料夾：
   ```
   cd 桌面/revenue-yoy-backtest
   ```
3. 執行程式：
   ```
   python 03_月營收YoY回測_指令輸入版.py
   ```
4. 看到輸入框後，輸入股票指令，按 Enter 開始回測

> 💡 `.ipynb` 要轉成 `.py`，在 Jupyter Notebook 點「**檔案**」→「**下載**」→「**下載 .py**」即可。

## ⚠️ 免責聲明

本專案僅供學術研究與程式教學用途，所有回測結果均基於歷史資料，不代表未來績效，不構成任何投資建議。投資有風險，請自行評估。

---

## 👨‍🏫 關於作者

本專案由**小龍蝦 AI 課程**提供，課程收入全數捐入基金會。
