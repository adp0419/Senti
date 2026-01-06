def generate_headline(ticker, price_data, sentiment_score):
    if sentiment_score > 0:
        direction = "positive"
    elif sentiment_score < 0:
        direction = "negative"
    else:
        direction = "neutral"
    return f"{ticker} | {price_data['percent_change']}% | {direction} sentiment"