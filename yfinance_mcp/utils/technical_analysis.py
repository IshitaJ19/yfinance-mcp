from yfinance import download as yf_download


async def get_technical_signals(ticker: str) -> dict:
    """Get technical signals and indicators for a given ticker by performing technical analysis"""
    
    try:
        df = yf_download(ticker, period="6mo", interval="1d", progress=False)
        df = df.droplevel("Ticker", axis=1).reset_index()

        if df.empty:
            return {"ticker": ticker, "error": "No data."}

       # Calculate RSI (14-day)
        delta = df["Close"].diff()
        gain = delta.where(delta > 0, 0).rolling(window=14).mean()
        loss = -delta.where(delta < 0, 0).rolling(window=14).mean()
        rs = gain / loss
        df["rsi"] = 100 - (100 / (1 + rs))

        # Calculate MACD and signal
        ema_12 = df["Close"].ewm(span=12, adjust=False).mean()
        ema_26 = df["Close"].ewm(span=26, adjust=False).mean()
        df["macd"] = ema_12 - ema_26
        df["macd_signal"] = df["macd"].ewm(span=9, adjust=False).mean()

        # Calculate SMA
        df["sma_20"] = df["Close"].rolling(window=20).mean()
        df["sma_50"] = df["Close"].rolling(window=50).mean()

        df = df.dropna()
        latest = df.iloc[-1].to_dict()

        # Interpret signals
        rsi = round(latest["rsi"], 2)
        macd_cross = latest["macd"] > latest["macd_signal"]
        sma_cross = latest["sma_20"] > latest["sma_50"]

        bullish = (30 < rsi < 70) and macd_cross and sma_cross

        interpretation = []
        if rsi > 70:
            interpretation.append("RSI indicates the stock is overbought.")
        elif rsi < 30:
            interpretation.append("RSI indicates the stock is oversold.")
        else:
            interpretation.append("RSI is in the neutral range.")

        interpretation.append(f"MACD crossover is {'bullish' if macd_cross else 'bearish'}.")
        interpretation.append(f"SMA 20/50 crossover is {'bullish' if sma_cross else 'bearish'}.")

        return {
            "ticker": ticker,
            "bullish": bullish,
            "rsi": rsi,
            "macd_crossover": "bullish" if macd_cross else "bearish",
            "sma_crossover": "bullish" if sma_cross else "bearish",
            "summary": " ".join(interpretation)
        }

    except Exception as e:
        return {"error": str(e)}
    

