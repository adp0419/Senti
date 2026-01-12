def analyze_sentiment(articles):
    if not articles:
        return 0
    
    # temporary keyword lists
    positive_keywords = ["bullish", "up", "strong", "beats", "growth", "peak"]
    negative_keywords = ["bearish", "down", "weak", "miss", "loss", "fall"]

    sentiment = 0

    for article in articles:
        text = article.get("headline", "").lower() + " " + article.get("summary", "").lower() 
        for word in positive_keywords:
            if word in text:
                sentiment += 1
        for word in negative_keywords:
            if word in text:
                sentiment -= 1
    
    return sentiment