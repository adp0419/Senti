def generate_headline(ticker, price_data, sentiment_score):
    # if sentiment_score > 0:
    #     direction = "positive"
    # elif sentiment_score < 0:
    #     direction = "negative"
    # else:
    #     direction = "neutral"
    # return f"{ticker} | {price_data['percent_change']}% | {direction} sentiment"

    if not price_data:
        return f"{ticker}: No price data available."
    
    if price_data['percent_change'] > 0:
        direction = "up"
    elif price_data['percent_change'] < 0:
        direction = "down"
    else:
        direction = "stable"

    if sentiment_score > 0:
        sentiment = "positive"
    elif sentiment_score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return (f"{ticker} is {direction} {abs(price_data['percent_change'])}% with {sentiment} news sentiment.")
