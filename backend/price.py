import yfinance as yf
# import pandas as pd - maybe for future use

def get_price_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        hpd = stock.history(period="5d") # historical price data for the last 5 days

        if hpd.empty: # if no data is found for inputted ticker
            return None 
        
        start_price = hpd['Close'].iloc[0]
        latest_price = hpd['Close'].iloc[-1]

        percent_change = ((latest_price - start_price) / start_price) * 100

        return {
            "ticker": ticker,
            "start_price": round(start_price, 2),
            "latest_price": round(latest_price, 2),
            "percent_change": round(percent_change, 2)
        }
    
    except Exception as e:
        print(f"ERROR: Could not find data for ticker {ticker}: {e}")
        return None
    


   
