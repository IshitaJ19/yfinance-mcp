from typing import Optional, Literal, List

from yfinance_mcp.data_models.outputs import (
    StockResult, 
    ScreenStocksOutput,
    MarketCap,
)
from yfinance_mcp.utils.finance import (
    get_matching_tickers, 
    get_stock_info,
    get_market_cap_bucket,
)
from yfinance_mcp.utils.technical_analysis import (
    get_technical_signals,
)


def get_market_cap(ticker: str) -> MarketCap:
    """Fetches market cap for a given ticker."""
    stock_info = get_stock_info(ticker)
    if stock_info:
        market_cap = stock_info.get("marketCap", None)
        bucket = get_market_cap_bucket(market_cap)
        return MarketCap(
            market_cap=market_cap,
            bucket=bucket
        )
    return MarketCap(
        market_cap=None,
        bucket="unknown"
    )

def screen_stocks(sector: str,
                  market_cap: Optional[Literal["small", "mid", "large"]] = None,
                  revenue_growth_lower_bound: Optional[float] = None,
                  margin_trend: Optional[Literal["improving", "declining", "flat"]] = None
                  ) -> ScreenStocksOutput:
    """Screen stocks based on sector, market cap, revenue growth, and margin trend."""
    matching_stocks = get_matching_tickers(
        sector=sector,
        market_cap=market_cap,
        revenue_growth_lower_bound=revenue_growth_lower_bound,
        margin_trend=margin_trend
    )

    stock_results = [
        StockResult(
            ticker=stock["ticker"],
            company=stock["company"],
            rev_growth=stock["rev_growth"],
            margin_trend=stock["margin_trend"],
            market_cap=stock["market_cap"]
        )
        for stock in matching_stocks
    ]

    return ScreenStocksOutput(results=stock_results)

def get_gross_margins(ticker: str) -> float:
    """Function to get gross margins for a ticker."""
    # This should be replaced with actual logic to fetch gross margins

    stock_info = get_stock_info(ticker)
    if stock_info:
        return stock_info.get("grossMargins", 0.0)
    return 0.0


async def screen_bullish_stocks(tickers: List[str]) -> dict:
    """Screen bullish stocks out of the given list of ticker symbols, 
    based on RSI, MACD and SMA crossovers."""

    results = []

    for ticker in tickers:
        try:
            signal = get_technical_signals(ticker)
            if signal.get("bullish"):
                results.append(signal)
        except Exception as e:
            results.append({"ticker": ticker, "error": str(e)})

    return {
        "bullish_tickers": results,
        "count": len(results),
    }