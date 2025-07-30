from fastmcp.server import FastMCP

# Import your tool module so decorated functions register automatically
from yfinance_mcp.utils.finance import (
    get_stock_info,
    get_ticker_financials,
)
from yfinance_mcp.utils.news import (
    get_news,
)
from yfinance_mcp.utils.technical_analysis import (
    get_technical_signals,
)
from yfinance_mcp.tools.screen_stocks import (
    screen_stocks, 
    get_gross_margins,
    get_market_cap,
    screen_bullish_stocks,
)


# Create FastMCP app instance   
mcp = FastMCP("Stock Screening App")

mcp.tool()(get_gross_margins)
mcp.tool()(screen_stocks)
mcp.tool()(get_market_cap)
mcp.tool()(get_ticker_financials)
mcp.tool()(get_stock_info)
mcp.tool()(get_news)

mcp.tool()(get_technical_signals)
mcp.tool()(screen_bullish_stocks)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
