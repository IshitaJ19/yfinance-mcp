import yfinance as yf
from typing import List, Optional, Literal, Dict

# Optional: Predefined stock universe (S&P 500, etc.)
from yfinance_mcp.utils.stock_universe import get_tickers_by_sector
from yfinance_mcp.utils.constants import MARKET_CAP_THRESHOLDS


def get_ticker_obj(ticker:str) -> Optional[yf.Ticker]:
    """Fetches ticker object using yfinance."""
    try:
        return yf.Ticker(ticker)
    except Exception as e:
        print(f"Error fetching ticker {ticker}: {e}")
        return None
    
def get_stock_info(ticker: str) -> Optional[dict]:
    """Fetches stock info using yfinance."""
    try:
        t = get_ticker_obj(ticker)
        info = t.info
        return {
            "ticker": ticker,
            "company": info.get("shortName", ""),
            "marketCap": info.get("marketCap", None),
            "sector": info.get("sector", ""),
            "grossMargins": info.get("grossMargins", None),
            "trailingPE": info.get("trailingPE", None),
            "forwardPE": info.get("forwardPE", None),
            "priceToBook": info.get("priceToBook", None),
            "debtToEquity": info.get("debtToEquity", None),
            "freeCashflow": info.get("freeCashflow", None),
            "earningsGrowth": info.get("earningsGrowth", None),
            "pegRatio": info.get("pegRatio", None),
            "dividendYield": info.get("dividendYield", None),
        }
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None
    

def get_ticker_financials(ticker: str) -> Optional[Dict]:
    """Fetches financials for a ticker."""
    try:
        t = get_ticker_obj(ticker)
        return t.financials.to_dict() if t else None
    except Exception as e:
        print(f"Error fetching financials for {ticker}: {e}")
        return None

def compute_revenue_growth(ticker_obj: yf.Ticker) -> Optional[float]:
    """Computes YoY revenue growth from income statement."""
    try:
        fin = ticker_obj.financials
        revenue = fin.loc["Total Revenue"]
        if len(revenue) < 2:
            return None
        latest = revenue.iloc[0]
        previous = revenue.iloc[1]
        if previous == 0:
            return None
        growth = (latest - previous) / previous * 100
        return round(growth, 2)
    except Exception:
        return None


def compute_margin_trend(ticker_obj: yf.Ticker) -> Optional[str]:
    """Determines if gross margin is improving, declining, or flat."""
    try:
        fin = ticker_obj.financials
        revenue = fin.loc["Total Revenue"]
        gross_profit = fin.loc["Gross Profit"]
        if len(revenue) < 2 or len(gross_profit) < 2:
            return None

        margin_0 = gross_profit.iloc[0] / revenue.iloc[0]
        margin_1 = gross_profit.iloc[1] / revenue.iloc[1]
        delta = margin_0 - margin_1

        if abs(delta) < 0.01:
            return "flat"
        return "improving" if delta > 0 else "declining"
    except Exception:
        return None


def get_market_cap_bucket(market_cap: Optional[int]) -> str:
    """Classifies market cap into 'small', 'mid', or 'large'."""
    if market_cap is None:
        return "unknown"
    if market_cap < MARKET_CAP_THRESHOLDS["small"]:
        return "small"
    elif market_cap < MARKET_CAP_THRESHOLDS["mid"]:
        return "mid"
    else:
        return "large"


def get_matching_tickers(
        sector: str,
        market_cap: Optional[Literal["small", "mid", "large"]] = None,
        revenue_growth_lower_bound: Optional[float] = None,    # e.g. ">10"
        margin_trend: Optional[Literal["improving", "declining", "flat"]] = None
) -> List[dict]:
    """Fetches stocks matching criteria using yfinance."""

    tickers = get_tickers_by_sector(sector)
    matches = []

    for symbol in tickers:
        try:
            t = yf.Ticker(symbol)
            info = t.info

            company_name = info.get("shortName", "")
            cap = info.get("marketCap", None)
            cap_bucket = get_market_cap_bucket(cap)

            if market_cap and cap_bucket != market_cap:
                continue

            rev_growth_val = compute_revenue_growth(t)
            if revenue_growth_lower_bound:
                try:
                    if rev_growth_val is None or rev_growth_val <= revenue_growth_lower_bound:
                        continue
                except ValueError:
                    continue

            margin_val = compute_margin_trend(t)
            if margin_trend and margin_val != margin_trend:
                continue

            matches.append({
                "ticker": symbol,
                "company": company_name,
                "rev_growth": f"{rev_growth_val:.2f}%" if rev_growth_val is not None else "N/A",
                "margin_trend": margin_val or "N/A",
                "market_cap": cap_bucket
            })

        except Exception:
            continue

    return matches
    