# yfinance-mcp
MCP Server for yfinance library

## To set up
1. Download and install `uv`
2. `uv venv .venv`
3. `uv pip install .`

## To run
`uv run -m yfinance_mcp.main`

## Run dev tests
`pytest`

## Run a test client
`uv run -m yfinance_mcp.test_client`

## References
- https://github.com/jlowin/fastmcp
- https://github.com/ranaroussi/yfinance
