def get_news_articles(ticker):
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