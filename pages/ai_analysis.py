import streamlit as st
import openai
import yfinance as yf
import pandas as pd

def get_ai_analysis(ticker, question):
    """
    Calls OpenAI's API to get an AI-generated analysis or answer for a given stock.
    """
    # If you're using secrets on Streamlit Cloud:
    openai.api_key = st.secrets["OPENAI_API_KEY"]  # or read from an environment variable

    prompt = f"""
    You are a financial expert. The user wants to know about the stock: {ticker}.
    Question: {question}

    Provide a concise, helpful response (not financial advice).
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def show_stock_data(ticker):
    """
    Fetch and display the recent 6 months of stock data from Yahoo Finance.
    """
    df = yf.download(ticker, period="6mo")
    if df.empty:
        st.error("No data found. Check the ticker symbol and try again.")
        return
    
    st.write(f"**Recent data for {ticker}**")
    st.dataframe(df.tail(5))

    # Simple line chart of the Close price
    st.line_chart(df["Close"])

def run_ai_analysis_page():
    st.title("AI Stock Analysis")
    st.write("Use OpenAI to get insights on a particular stock.")
    
    ticker = st.text_input("Enter Stock Ticker", value="AAPL")
    user_question = st.text_area("Your question", value="What's the short-term outlook?")
    
    if st.button("Analyze with AI"):
        with st.spinner("Asking OpenAI..."):
            analysis = get_ai_analysis(ticker, user_question)
        st.success("AI Response:")
        st.write(analysis)
    
    st.write("---")
    st.subheader("Stock Price Data")
    show_stock_data(ticker)

# When this file is run as a page, Streamlit automatically calls it:
if __name__ == "__main__":
    run_ai_analysis_page()
