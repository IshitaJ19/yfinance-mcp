# YFinance MCP Server

A Model Context Protocol (MCP) server for comprehensive stock analysis and screening using Yahoo Finance data. This server provides tools for financial analysis, technical indicators, news aggregation, and stock screening capabilities.

## Features

### 📊 Financial Analysis
- **Stock Information**: Get comprehensive stock data including market cap, P/E ratios, margins, and financial metrics
- **Financial Statements**: Access detailed financial data and statements
- **Revenue Growth Analysis**: Calculate year-over-year revenue growth
- **Margin Trend Analysis**: Track gross margin improvements/declines

### 🔍 Stock Screening
- **Sector-based Screening**: Filter stocks by sector (Technology, Healthcare, Finance)
- **Market Cap Classification**: Small (<$2B), Mid ($2B-$10B), Large (>$10B)
- **Growth Screening**: Filter by revenue growth thresholds
- **Margin Trend Filtering**: Screen for improving/declining margins

### 📈 Technical Analysis
- **RSI (Relative Strength Index)**: 14-day RSI calculation
- **MACD**: Moving Average Convergence Divergence with signal line
- **SMA Crossovers**: 20-day and 50-day Simple Moving Averages
- **Bullish Signal Detection**: Combined technical indicator analysis

### 📰 News & Content
- **Stock News**: Latest news articles for any ticker
- **Content Extraction**: Automated news content parsing
- **Multi-source News**: Aggregated from multiple financial sources

## Installation

### Prerequisites
- Python 3.13+
- pip or uv package manager

### Setup
```bash
# Clone the repository
git clone <repository-url>
cd yfinance-mcp-main

# Install dependencies
pip install -e .

# Or using uv (recommended)
uv sync
```

## Usage

### Starting the Server
```bash
# Run the MCP server
python -m yfinance_mcp.main

# Or using the entry point
start
```

The server will start on `http://127.0.0.1:8000/mcp`

### Available Tools

#### 1. Stock Information
```python
get_stock_info(ticker: str) -> dict
```
Returns comprehensive stock data including company info, financial metrics, and ratios.

#### 2. Stock Screening
```python
screen_stocks(
    sector: str,
    market_cap: Optional["small" | "mid" | "large"] = None,
    revenue_growth_lower_bound: Optional[float] = None,
    margin_trend: Optional["improving" | "declining" | "flat"] = None
) -> ScreenStocksOutput
```
Screens stocks based on multiple criteria and returns matching results.

#### 3. Technical Analysis
```python
get_technical_signals(ticker: str) -> dict
```
Performs technical analysis and returns RSI, MACD, and SMA crossover signals.

#### 4. News Analysis
```python
get_news(ticker: str) -> str
```
Fetches and parses latest news articles for a given ticker.

#### 5. Market Cap Analysis
```python
get_market_cap(ticker: str) -> MarketCap
```
Returns market cap value and classification bucket.

#### 6. Bullish Stock Screening
```python
screen_bullish_stocks(tickers: List[str]) -> dict
```
Screens a list of tickers for bullish technical signals.

## API Examples

### Get Stock Information
```python
# Get comprehensive data for Apple
stock_data = get_stock_info("AAPL")
# Returns: company name, market cap, sector, P/E ratios, margins, etc.
```

### Screen Technology Stocks
```python
# Find large-cap tech stocks with >10% revenue growth
results = screen_stocks(
    sector="Technology",
    market_cap="large",
    revenue_growth_lower_bound=10.0
)
```

### Technical Analysis
```python
# Get technical signals for a stock
signals = get_technical_signals("TSLA")
# Returns: RSI, MACD crossover, SMA crossover, bullish/bearish summary
```

### News Analysis
```python
# Get latest news for a stock
news = get_news("MSFT")
# Returns: Latest news articles with titles, links, and content
```

## Project Structure

```
yfinance-mcp-main/
├── yfinance_mcp/
│   ├── main.py                 # MCP server entry point
│   ├── data_models/
│   │   └── outputs.py         # Pydantic models for responses
│   ├── tools/
│   │   └── screen_stocks.py   # Stock screening tools
│   └── utils/
│       ├── constants.py       # Market cap thresholds
│       ├── finance.py         # Core financial analysis
│       ├── news.py           # News aggregation
│       ├── stock_universe.py # Stock universe management
│       └── technical_analysis.py # Technical indicators
├── tests/                     # Test suite
├── pyproject.toml            # Project configuration
└── README.md
```

## Dependencies

- **fastmcp**: MCP server framework
- **yfinance**: Yahoo Finance data access
- **pydantic**: Data validation and serialization
- **requests**: HTTP requests for news
- **beautifulsoup4**: HTML parsing for news content

## Testing

Run the test suite:
```bash
pytest tests/
```

## Development

### Adding New Tools
1. Create your function in the appropriate utils module
2. Import and register it in `main.py` using `@mcp.tool()`
3. Add tests in the `tests/` directory

### Extending Stock Universe
Update `utils/stock_universe.py` to include more sectors and tickers.

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
