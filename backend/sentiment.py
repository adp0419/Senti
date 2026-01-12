from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

labels = ["negative", "neutral", "positive"]


def analyze_sentiment(articles):
    results = []

    if not articles: # handles stocks with no news articles
        return []

    for article in articles:
        text = f"{article.get('headline', '')} {article.get('summary', '')}"
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

    with torch.no_grad(): # since we are not training a model we do not need to calculate gradients
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)[0]
    
    sentiment = {
        "positive": probs[2].item(),
        "neutral": probs[1].item(),
        "negative": probs[0].item()
    }
    
    results.append({
        **article,
        "sentiment": sentiment
    })

    return results 

def aggregate_sentiment(scored_articles): # returns a score influence by the number of articles about the stock (as more/less news on a stock can indicate sentiment too)
    if not scored_articles:
        return 0.0
    
    score = 0

    for a in scored_articles:
        score += a["sentiment"]["positive"] - a["sentiment"]["negative"]

    return score / len(scored_articles)

def keyword_sentiment(articles): # old simple sentiment analysis using rule-based keyword matching | never use this function
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
    
if __name__ == "__main__":
    # Sample test articles
    sample_articles = [
        {
            "headline": "AAPL beats quarterly earnings expectations",
            "summary": "Apple has exceeded analyst expectations this quarter, showing strong growth in iPhone sales.",
            "source": "Financial Times",
            "date": "2026-01-03",
            "url": "https://example.com/article1"
        },
        {
            "headline": "AAPL faces supply chain issues",
            "summary": "Delays in the supply chain may affect Apple's production and revenue in the coming months.",
            "source": "Bloomberg",
            "date": "2026-01-02",
            "url": "https://example.com/article2"
        }
    ]

    scored = analyze_sentiment(sample_articles)
    for article in scored:
        print(f"Headline: {article['headline']}")
        print(f"Sentiment: {article['sentiment']}")
        print("-----------")

    agg_score = aggregate_sentiment(scored)
    print(f"Aggregated Sentiment Score: {agg_score:.3f}")