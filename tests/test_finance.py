from yfinance_mcp.utils.finance import (
    get_matching_tickers, 
    get_stock_info,
    get_market_cap_bucket
)

from yfinance_mcp.tools.screen_stocks import (
    screen_stocks,
    get_gross_margins,
    get_market_cap,
)

from yfinance_mcp.utils.technical_analysis import (
    get_technical_signals,
)

def test_get_stock_info():
    """Test fetching stock info for a valid ticker."""
    ticker = "AAPL"
    stock_info = get_stock_info(ticker)
    assert stock_info is not None
    assert stock_info["ticker"] == ticker
    assert "company" in stock_info
    assert "marketCap" in stock_info
    assert "sector" in stock_info
    assert "grossMargins" in stock_info

def test_get_market_cap():
    """Test fetching market cap for a valid ticker."""
    ticker = "GOOGL"
    info = get_market_cap(ticker)
    assert info.market_cap is not None
    assert isinstance(info.market_cap, int) or info.market_cap  is None
    assert info.bucket in ["small", "mid", "large", "unknown"]


async def test_get_technical_signals():
    """Test fetching technical signals for a valid ticker."""

    ticker = "INTL"
    tech_signals = await get_technical_signals(ticker)
    print(tech_signals)

if __name__ == "__main__":
    import asyncio

    asyncio.run(test_get_technical_signals())
    