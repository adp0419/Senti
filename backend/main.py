from price import *
from news import *
from sentiment import *
from headline import *

print("This project will analyze stock news sentiment and be a source of information for why a stock is moving how it is.")
print("Input as many stock tickers you want. Press [enter] when done.")
ticker_list = []

while True:
   
   ticker = input("> ").strip().upper()
   
   if ticker == "":
        if len(ticker_list) == 0:
            print("You must input at least one ticker.")
            continue
        break
   
   if ticker in ticker_list:
        print("Ticker already added. Please input a different ticker or press [enter] to finish.")
        continue
   
   if not ticker.isalpha():
        print("Tickers cannot contain non-alphabetic characters. Please input a valid stock ticker.")
        continue
   
   ''' 
    WILL WRITE LATER - Check is ticker is a real stock ticker
    if not valid_ticker(ticker):
        print("Ticker not found. Please input a valid stock ticker.")
    '''
   
   ticker_list.append(ticker)

print("Processing Tickers...")

for ticker in ticker_list:
    price = get_price_data(ticker)
    articles = get_news_articles(ticker)
    sentiment_score = analyze_sentiment(articles)
    insight = generate_insight(ticker, price, sentiment_score)
    print(insight)