import os
from dotenv import load_dotenv
import finnhub as fh
import datetime

load_dotenv()

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

def get_fake_news(ticker): # old function using fake news before I implemented API calls for real news
    # return [
    #     {"title": "Fake headline 1", "source": "Source A", "date": "2026-01-03", "url": "https://example.com"},
    #     {"title": "Fake headline 2", "source": "Source B", "date": "2026-01-02", "url": "https://example.com"},
    # ]

    # for now will return fake articles for testing purposes

    fake_news = [
        {"title": f"{ticker} beats quarterly earnings expectations",
         "source": "The Financial Times",
         "date": "2026-01-03",
         "link": "https://example.com/article1"},
        {"title": f"{ticker} announces new product launch",
         "source": "Bloomberg",
         "date": "2026-01-02",
         "link": "https://example.com/article2"},
        {"title": f"Investors bullish on {ticker} stock after market rally",
         "source": "CNBC",
         "date": "2026-01-01",
         "link": "https://example.com/article3"}
    ]

    return fake_news

def get_news_articles(ticker): # pulling articles from Finnhub Company News API
    finnhub_client = fh.Client(api_key=FINNHUB_API_KEY)
    
    
    print(finnhub_client.general_news('general', min_id=0)) # temporary print to check if API is working


if __name__ == "__main__":
    ticker = "AAPL"  # pick any ticker to test
    import pprint
    articles = get_news_articles(ticker)
    pprint.pprint(articles)