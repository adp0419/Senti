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

    if sentiment_score >= 3:
        sentiment = "strongly positive"
    elif sentiment_score > 0:
        sentiment = "slightly positive"
    elif sentiment_score == 0:
        sentiment = "mixed"
    elif sentiment_score > -3:
        sentiment = "slightly negative"
    else:
        sentiment = "strongly negative"

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
        f"{ticker} is {direction} {abs(price_data['percent_change']):.2f}% over the selected time period.\n"
        f"Recent news sentiment is {sentiment}, based on current headlines.\n"
        f"{interpretation}"
    )


