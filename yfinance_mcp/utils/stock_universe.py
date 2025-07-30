# mcp_server/utils/stock_universe.py
from typing import List

def get_tickers_by_sector(sector: str) -> List[str]:
    """Returns tickers for a sector. Replace with real data or API later."""
    sample_universe = {
        "Technology": ["AAPL", "MSFT", "GOOGL", "NVDA"],
        "Healthcare": ["JNJ", "PFE", "UNH"],
        "Finance": ["JPM", "BAC", "WFC"]
    }
    return sample_universe.get(sector, [])
