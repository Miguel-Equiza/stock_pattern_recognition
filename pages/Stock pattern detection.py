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

with st.form("fitness_form"):
    # Accepting dropdown inputs for list-based variables
    ticker = st.selectbox("Select the ticker", ["GOOGL", "TSLA"], index=0)
    start_date = st.date_input("Start date: YYYY-MM-DD", value=datetime(2019, 11, 3))
    
    max_end_date = start_date + timedelta(days=450)
    end_date = st.date_input("End date: YYYY-MM-DD", min_value=start_date + timedelta(days=450), max_value=max_end_date)

    with_candle = st.selectbox("Do you want candle types to appear?", [True, False], index=0)
    candle_patterns = st.multiselect("Choose candle patterns", options=candle_types)
    # Submit button
    submitted = st.form_submit_button("Submit")


if submitted:
    
    plotting(ticker = ticker, start_date = start_date, end_date = end_date, with_candle = with_candle, cdle_patterns = candle_patterns)