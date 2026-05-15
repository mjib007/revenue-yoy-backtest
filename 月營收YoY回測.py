# -*- coding: utf-8 -*-
"""
📊 月營收 YoY 回測分析
🦞 小龍蝦 OpenClaw 學習教材

執行方式：
    python 月營收YoY回測.py

指令範例：
    2330.TW 月營收 20% 持有20天
    2640.TWO 月營收 15% 10天 20天 30天
    2317.TW 月營收 25%
"""

# ── 安裝套件（第一次執行時自動安裝）────────────────────
import subprocess, sys
subprocess.run(
    [sys.executable, "-m", "pip", "install",
     "requests", "pandas", "yfinance", "matplotlib", "-q"],
    check=True
)

import requests
import yfinance as yf
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import platform, warnings, re
warnings.filterwarnings("ignore")

# ── 字型設定（Windows 用微軟正黑體，Mac/Linux 用預設）──
if platform.system() == "Windows":
    matplotlib.rc("font", family="Microsoft JhengHei")
elif platform.system() == "Darwin":
    matplotlib.rc("font", family="Heiti TC")
matplotlib.rcParams["axes.unicode_minus"] = False


# ── 解析指令 ──────────────────────────────────────────
def parse_command(cmd):
    """
    從自然語言指令解析參數
    支援格式：
      2330.TW 月營收 20% 持有20天
      2640.TWO 月營收 15% 10天 20天 30天
    """
    cmd = cmd.strip()

    # 抓 ticker（2330.TW 或 2640.TWO）
    ticker_match = re.search(r'(\d{4,}\.TWO?)', cmd, re.IGNORECASE)
    if not ticker_match:
        return None, None, None, None

    ticker_full = ticker_match.group(0).upper()
    # 先換 .TWO 再換 .TW，避免 2640.TWO → 2640O
    stock_id = ticker_full.replace(".TWO", "").replace(".TW", "")
    market   = "TWO" if "TWO" in ticker_full else "TW"

    # 抓 YoY 門檻（數字+%）
    yoy_match = re.search(r'(\d+(?:\.\d+)?)\s*%', cmd)
    yoy_threshold = float(yoy_match.group(1)) if yoy_match else 20.0

    # 抓持有天數（可多個）
    days = [int(d) for d in re.findall(r'(\d+)\s*天', cmd)]
    if not days:
        days = [5, 10, 20, 30]   # 預設觀察四個窗口

    return stock_id, market, yoy_threshold, days


# ── 回測主函式 ─────────────────────────────────────────
def run_revenue_backtest(stock_id, market, yoy_threshold, windows,
                         start_date="2015-01-01", end_date="2025-12-31",
                         finmind_token=""):
    """
    月營收 YoY 回測
    stock_id      : 股票代號（不含後綴），例如 2330
    market        : TW（上市）或 TWO（上櫃）
    yoy_threshold : YoY 觸發門檻（%）
    windows       : 持有天數清單，例如 [5, 10, 20, 30]
    start_date    : 回測起始日期
    end_date      : 回測結束日期
    finmind_token : FinMind Token（可留空）
    """

    print(f"\n⏳ 抓取 {stock_id}.{market} 月營收資料...")

    # Step 1：從 FinMind 抓月營收
    params = {
        "dataset":    "TaiwanStockMonthRevenue",
        "data_id":    stock_id,
        "start_date": start_date,
        "end_date":   end_date,
    }
    if finmind_token:
        params["token"] = finmind_token

    resp = requests.get(
        "https://api.finmindtrade.com/api/v4/data",
        params=params, timeout=30
    )
    data = resp.json()

    if data.get("status") != 200:
        print(f"❌ FinMind 抓取失敗：{data.get('msg')}")
        return

    rev = pd.DataFrame(data["data"])
    if rev.empty:
        print(f"❌ FinMind 無 {stock_id} 的月營收資料")
        return

    rev["date"]        = pd.to_datetime(rev["date"])
    rev                = rev.sort_values("date").reset_index(drop=True)
    # FinMind 的 date 欄位是公告日期（次月初），往前推一個月才是真正的營收月份
    rev["revenue_month"] = rev["date"] - pd.DateOffset(months=1)
    rev["revenue_yoy"]   = rev["revenue"].pct_change(12) * 100
    rev                  = rev.dropna(subset=["revenue_yoy"]).reset_index(drop=True)
    print(f"✅ 月營收：共 {len(rev)} 筆（{rev['date'].min().date()} ～ {rev['date'].max().date()}）")

    # Step 2：從 yfinance 抓股價，計算公告日（次月10日）
    ticker = f"{stock_id}.{market}"
    print(f"⏳ 下載 {ticker} 股價...")
    price_df = yf.download(
        ticker, start=start_date, end=end_date,
        auto_adjust=True, progress=False
    )
    if isinstance(price_df.columns, pd.MultiIndex):
        price_df.columns = price_df.columns.get_level_values(0)
    price_df = price_df[["Close"]].copy()

    if price_df.empty:
        print(f"❌ 無法取得 {ticker} 股價，請確認代號是否正確")
        return

    print(f"✅ 股價：共 {len(price_df)} 筆（{price_df.index.min().date()} ～ {price_df.index.max().date()}）")

    def get_announce_date(revenue_date):
        next_month = revenue_date + pd.DateOffset(months=1)
        announce   = pd.Timestamp(next_month.year, next_month.month, 10)
        future     = price_df.index[price_df.index >= announce]
        return future[0] if len(future) > 0 else None

    rev["announce_date"] = rev["date"].apply(get_announce_date)
    rev = rev.dropna(subset=["announce_date"]).reset_index(drop=True)

    # Step 3：篩選 YoY 超過門檻的觸發點
    signals = rev[rev["revenue_yoy"] > yoy_threshold].copy()
    if signals.empty:
        print(f"❌ YoY 從未超過 {yoy_threshold}%，無觸發樣本")
        return

    print(f"\nYoY > {yoy_threshold}% 的月份共 {len(signals)} 次")

    # Step 4：多時間窗口勝率計算
    hold_days = windows[0]
    results   = []
    for _, row in signals.iterrows():
        buy_idx  = price_df.index.get_loc(row["announce_date"])
        sell_idx = buy_idx + hold_days
        if sell_idx < len(price_df):
            bp = price_df["Close"].iloc[buy_idx]
            sp = price_df["Close"].iloc[sell_idx]
            results.append({
                "revenue_month": row["date"],
                "announce_date": row["announce_date"],
                "yoy":           row["revenue_yoy"],
                "buy_price":     bp,
                "sell_price":    sp,
                "return_pct":    (sp - bp) / bp * 100
            })

    result_df = pd.DataFrame(results)

    # 印出勝率表
    print(f"\n{'='*50}")
    print(f"  {stock_id}　YoY > {yoy_threshold}%　多時間窗口勝率")
    print(f"{'='*50}")
    print(f"  {'持有天數':>8} {'勝率':>8} {'平均報酬':>10} {'樣本數':>8}")
    print(f"  {'-'*38}")
    for w in windows:
        w_results = []
        for _, row in signals.iterrows():
            buy_idx  = price_df.index.get_loc(row["announce_date"])
            sell_idx = buy_idx + w
            if sell_idx < len(price_df):
                bp = price_df["Close"].iloc[buy_idx]
                sp = price_df["Close"].iloc[sell_idx]
                w_results.append((sp - bp) / bp * 100)
        if w_results:
            wr    = sum(1 for r in w_results if r > 0) / len(w_results) * 100
            ar    = sum(w_results) / len(w_results)
            emoji = "📈" if wr > 50 else "📉"
            print(f"  {w:>5} 天後  {emoji} {wr:>5.1f}%  {ar:>+8.2f}%  {len(w_results):>6}")
    print(f"{'='*50}")

    if not result_df.empty:
        print("\n各年觸發次數：")
        print(result_df["revenue_month"].dt.year.value_counts().sort_index().to_string())

    # Step 5：視覺化
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 9), sharex=False)

    ax1.plot(price_df.index, price_df["Close"],
             color="#1f77b4", linewidth=1, label="收盤價")
    if not result_df.empty:
        ax1.scatter(
            result_df["announce_date"], result_df["buy_price"],
            color="red", marker="v", s=80, zorder=5,
            label=f"買入點（YoY>{yoy_threshold}%，共{len(result_df)}次）"
        )
    ax1.set_title(f"{stock_id} 股價走勢與月營收 YoY 觸發點", fontsize=13)
    ax1.set_ylabel("股價（元）")
    ax1.legend()
    ax1.grid(alpha=0.3)

    colors = ["green" if v > 0 else "red" for v in rev["revenue_yoy"]]
    ax2.bar(rev["announce_date"], rev["revenue_yoy"],
            color=colors, width=20, alpha=0.7)
    ax2.axhline(yoy_threshold, color="orange", linewidth=1.5,
                linestyle="--", label=f"門檻 {yoy_threshold}%")
    ax2.axhline(0, color="black", linewidth=0.8)
    ax2.set_title(f"{stock_id} 月營收 YoY（%）", fontsize=13)
    ax2.set_ylabel("YoY (%)")
    ax2.legend()
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    plt.show()
    print("\n✅ 完成！")


# ── 主程式 ────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("  📊 月營收 YoY 回測分析")
    print("  🦞 小龍蝦 OpenClaw 學習教材")
    print("=" * 50)
    print()
    print("指令格式：<股票代號> 月營收 <YoY門檻%> [持有天數]")
    print()
    print("範例：")
    print("  2330.TW 月營收 20% 持有20天")
    print("  2640.TWO 月營收 15% 10天 20天 30天")
    print("  2317.TW 月營收 25%")
    print()

    while True:
        user_input = input("請輸入指令（輸入 q 離開）：").strip()

        if user_input.lower() in ["q", "quit", "exit", "離開"]:
            print("👋 再見！")
            break

        if not user_input:
            continue

        stock_id, market, yoy_threshold, windows = parse_command(user_input)

        if not stock_id:
            print("❌ 無法識別股票代號，請輸入如 2330.TW 或 2640.TWO")
            continue

        print(f"\n解析結果：{stock_id}.{market} | YoY>{yoy_threshold}% | 觀察 {windows} 天")
        run_revenue_backtest(stock_id, market, yoy_threshold, windows)
        print()
