def generate_insight(ticker, price_data, sentiment_score):
    if sentiment_score > 0:
        direction = "positive"
    elif sentiment_score < 0:
        direction = "negative"
    else:
        direction = "neutral"
    return f"{ticker} | {price_data['change_pct']}% | {direction} sentiment"