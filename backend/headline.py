def generate_headline(ticker, price_data, sentiment_score):
    
    if not price_data:
        return f"{ticker}: No price data available."
    
    if price_data['percent_change'] > 0:
        direction = "up"
    elif price_data['percent_change'] < 0:
        direction = "down"
    else:
        direction = "stable"

    if sentiment_score >= 0.4:
        sentiment = "strongly positive"
    elif sentiment_score >= 0.1:
        sentiment = "slightly positive"
    elif sentiment_score <= -0.4:
        sentiment = "strongly negative"
    elif sentiment_score <= -0.1:
        sentiment = "slightly negative"
    else:
        sentiment = "neutral"

    if direction == "up" and sentiment in ["strongly positive", "slightly positive"]:
        interpretation = "news-driven rally"
    elif direction == "down" and sentiment in ["strongly negative", "slightly negative"]:
        interpretation = "bearish narrative"
    elif direction == "up" and sentiment in ["strongly negative", "slightly negative"]:
        interpretation = "technical rebound / lagging news"
    elif direction == "down" and sentiment in ["strongly positive", "slightly positive"]:
        interpretation = "overreaction / profit-taking"
    else:
        interpretation = "uncertainty / consolidation"

    return (
        f"{ticker} | {price_data['latest_price']} | {abs(price_data['percent_change']):.2f}%\n"
        f"Sentiment Score: {sentiment_score}\n"
        f"Interpretation: Based on current headlines, recent news sentiment is {sentiment}.\n"
        f"This indicates a potenital {interpretation}.\n"
    )