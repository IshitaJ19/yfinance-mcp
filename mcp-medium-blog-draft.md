# Building a Real-Time Stock Analysis Server with Model Context Protocol (MCP)

Ever wondered how to give AI models access to real-time financial data? I built an open-source project that does exactly that—using the Model Context Protocol (MCP) to create a powerful stock analysis server. Let me walk you through how it works and why it's a game-changer for financial AI applications.

## The Problem: AI Models Need Real Data

Traditional language models are great at explaining concepts, but they can't access real-time stock prices, financial statements, or market news. When someone asks "What's the current P/E ratio of Apple?" or "Show me tech stocks with high revenue growth," the model is limited to its training data—which might be months or years old.

That's where MCP (Model Context Protocol) comes in. It's an open standard that lets AI models call external tools and APIs in real-time. I decided to build something practical: a stock analysis server that exposes Yahoo Finance data through MCP.

## What I Built: YFinance MCP Server

My project creates an MCP server that provides 8 different stock analysis tools, all powered by Yahoo Finance data. Here's what it can do:

### 1. Stock Information & Financial Metrics
```python
# Get comprehensive data for any stock
stock_data = get_stock_info("AAPL")
# Returns: company name, market cap, sector, P/E ratios, margins, etc.
```

The server fetches real-time data including:
- Market capitalization and sector classification
- P/E ratios (trailing and forward)
- Gross margins and debt-to-equity ratios
- Free cash flow and earnings growth
- Dividend yields and PEG ratios

### 2. Intelligent Stock Screening
```python
# Find large-cap tech stocks with >10% revenue growth
results = screen_stocks(
    sector="Technology",
    market_cap="large",
    revenue_growth_lower_bound=10.0
)
```

The screening engine can filter stocks by:
- **Sector**: Technology, Healthcare, Finance (easily extensible)
- **Market Cap**: Small (<$2B), Mid ($2B-$10B), Large (>$10B)
- **Revenue Growth**: Year-over-year growth thresholds
- **Margin Trends**: Improving, declining, or flat gross margins

### 3. Technical Analysis with Multiple Indicators
```python
# Get technical signals for any stock
signals = get_technical_signals("TSLA")
# Returns: RSI, MACD crossover, SMA crossover, bullish/bearish summary
```

The technical analysis includes:
- **RSI (14-day)**: Relative Strength Index for overbought/oversold detection
- **MACD**: Moving Average Convergence Divergence with signal line
- **SMA Crossovers**: 20-day vs 50-day Simple Moving Averages
- **Combined Signals**: Bullish/bearish classification based on all indicators

### 4. News Aggregation & Content Parsing
```python
# Get latest news with content extraction
news = get_news("MSFT")
# Returns: Latest news articles with titles, links, and parsed content
```

The news system:
- Fetches the latest 3 news articles for any ticker
- Extracts and parses article content automatically
- Provides both headlines and full article text
- Handles multiple financial news sources

## How the Architecture Works

The project is built with a clean, modular architecture:

```
yfinance-mcp-main/
├── yfinance_mcp/
│   ├── main.py                 # MCP server entry point
│   ├── data_models/
│   │   └── outputs.py         # Pydantic models for responses
│   ├── tools/
│   │   └── screen_stocks.py   # Stock screening tools
│   └── utils/
│       ├── finance.py         # Core financial analysis
│       ├── technical_analysis.py # Technical indicators
│       ├── news.py           # News aggregation
│       └── stock_universe.py # Stock universe management
```

### Key Technical Decisions

1. **FastMCP Framework**: Used FastMCP for easy tool registration and HTTP transport
2. **Pydantic Models**: Structured data validation for all responses
3. **Error Handling**: Graceful handling of API failures and missing data
4. **Async Support**: Technical analysis functions are async for better performance

## Real-World Use Cases

Here are some practical scenarios where this MCP server shines:

### Scenario 1: Finding Growth Stocks
*User asks: "Show me mid-cap healthcare stocks with improving margins"*

The AI model can:
1. Call `screen_stocks(sector="Healthcare", market_cap="mid", margin_trend="improving")`
2. Get a list of matching stocks with their financial metrics
3. For each stock, call `get_technical_signals()` to check technical indicators
4. Fetch recent news with `get_news()` for context
5. Present a comprehensive analysis

### Scenario 2: Technical Analysis Workflow
*User asks: "Which of these stocks look bullish: AAPL, MSFT, GOOGL?"*

The model can:
1. Call `screen_bullish_stocks(["AAPL", "MSFT", "GOOGL"])`
2. Get technical analysis for each stock
3. Filter to only bullish candidates
4. Provide reasoning based on RSI, MACD, and SMA crossovers

### Scenario 3: Market Research
*User asks: "What's happening with Tesla stock?"*

The model can:
1. Get current financial data with `get_stock_info("TSLA")`
2. Check technical indicators with `get_technical_signals("TSLA")`
3. Fetch latest news with `get_news("TSLA")`
4. Provide a comprehensive market analysis

## Why This Matters for AI Development

This project demonstrates several important principles:

1. **Real-Time Data Access**: AI models can now access current financial data instead of relying on outdated training data
2. **Modular Design**: Each tool is independent and can be used in combination
3. **Extensible Architecture**: Easy to add new sectors, indicators, or data sources
4. **Production Ready**: Includes proper error handling, data validation, and testing

## Getting Started

The project is open source and easy to set up:

```bash
# Clone and install
git clone <your-repo>
cd yfinance-mcp-main
pip install -e .

# Run the server
python -m yfinance_mcp.main
```

The server starts on `http://127.0.0.1:8000/mcp` and any MCP-compatible AI model can discover and use the tools.

## What's Next

I'm planning to extend this project with:
- More sectors and stock universes
- Additional technical indicators (Bollinger Bands, Stochastic Oscillator)
- Historical data analysis capabilities
- Portfolio tracking and performance metrics
- Integration with other financial APIs

## The Bigger Picture

This project shows how MCP can transform AI applications from static chatbots into dynamic, data-driven assistants. Instead of saying "I don't have access to current stock data," the AI can now provide real-time financial analysis, screen stocks based on complex criteria, and give actionable investment insights.

The beauty of MCP is that once you build these tools, any compatible AI model can use them—whether it's GPT-4, Claude, or an open-source LLM. This democratizes access to powerful financial analysis capabilities.

---

**Want to contribute or build something similar?** Check out the [GitHub repository](#) and feel free to fork, extend, or use this as a template for your own MCP projects!

*What financial analysis tools would you like to see added to this server?* 