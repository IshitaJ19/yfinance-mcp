from pydantic import BaseModel
from typing import List


class StockResult(BaseModel):
    """Model for individual stock results."""

    ticker: str
    company: str
    rev_growth: str
    margin_trend: str
    market_cap: str

class ScreenStocksOutput(BaseModel):
    """Output model for screening stocks."""

    results: List[StockResult]
    
class MarketCap(BaseModel):
    """Model for market cap information."""

    market_cap: int
    bucket: str
    