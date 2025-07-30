import requests
from bs4 import BeautifulSoup
import yfinance as yf


def get_news_content(url: str) -> str:
    """Fetches news content from a given URL."""

    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    content = ' '.join([para.get_text() for para in paragraphs])
    return content  


def get_news(ticker: str) -> str:
    """Fetches the last 5 news articles for a given ticker from yfinance."""
    
    try:
        t = yf.Ticker(ticker)
        news_items = t.news
        if not news_items:
            return "No news available for this ticker."
        
        news_content = []
        for item in news_items[:3]:
            try:
                title = item.get('title', 'No title')
                url = item.get("content").get("canonicalUrl").get("url")
                content = get_news_content(url) if url else 'No content available'
                news_content.append(f"Title: {title}\nLink: {url}\nContent: {content}\n")
            except Exception as e:
                return Exception("Error fetching data")
        
        return "\n".join(news_content)[:240000]
    
    except Exception as e:
        return f"Error fetching news for {ticker}: {e}"