import streamlit as st
import yfinance as yf
import pandas as pd

def main():
    st.title("Simple Stock Tracker")
    st.write("Enter a stock ticker below (e.g. AAPL, TSLA, MSFT) to see its recent price chart.")

    # Text input for the user to enter a ticker
    ticker_symbol = st.text_input("Stock Ticker:", "AAPL")

    # Fetch data only when user clicks the button
    if st.button("Fetch Data"):
        st.write(f"Fetching data for {ticker_symbol}...")
        
        # Download 1 year of historical data from Yahoo Finance
        df = yf.download(ticker_symbol, period="1y", progress=False)
        
        if df.empty:
            st.error("No data found. Check the ticker symbol and try again.")
        else:
            st.success(f"Data found! Showing closing prices for {ticker_symbol}.")
            # Show a quick dataframe preview
            st.dataframe(df.tail(5))
            
            # Plot closing price
            st.line_chart(df['Close'])

if __name__ == "__main__":
    main()

