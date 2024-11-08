import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime, timedelta
from popping_model_logic import *

# Set up a form to accept all input variables
st.title("Enter stock market data")

candle_types = ['doji',
       'o_marubozu', 'gravestone', 'dragonfly_doji', 'hammer', 'c_marubozu',
       'bear_engulfing', 'bull_engulfing', 'tweezer_bottom', 'tweezer_top',
       'morning_star', 'evening_star', 'three_inside_up', 'three_inside_down',
       'three_black_crows', 'three_white_soldiers']

popular_tickers = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "BRK-B", "JPM",
    "V", "JNJ", "WMT", "PG", "DIS", "MA", "NFLX", "XOM", "PFE", "KO", "PEP",
    "CSCO", "INTC", "MRK", "HD", "VZ", "ADBE", "PYPL", "CRM", "NKE", "MCD"
]

with st.form("fitness_form"):
    # Accepting dropdown inputs for list-based variables
    ticker = st.selectbox("Select the ticker", popular_tickers, index=0)

    st.write("Those above are some of the most popular tickers, to see all available tickers see: https://investexcel.net/all-yahoo-finance-stock-tickers/ ")

    st.write("If you want to try with a different ticker, please enter it below")
    custom_ticker = st.text_input("If you enter an invalid ticker this will result in an error")

    start_date = st.date_input("Start date: YYYY-MM-DD", value=datetime(2019, 11, 3))

    max_end_date = start_date + timedelta(days=450)
    end_date = st.date_input("End date: YYYY-MM-DD", min_value=start_date + timedelta(days=10), max_value=max_end_date)

    with_candle = st.selectbox("Do you want candle types to appear?", [True, False], index=0)
    candle_patterns = st.multiselect("Choose candle patterns", options=candle_types)
    # Submit button
    submitted = st.form_submit_button("Submit")


if submitted:
    if custom_ticker:
        ticker = custom_ticker

    plotting(ticker = ticker, start_date = start_date, end_date = end_date, with_candle = with_candle, cdle_patterns = candle_patterns)
