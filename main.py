import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import streamlit as st
import pandas as pd

## Data selection 
# df = yf.download('AAPL', start='2019-01-01', end='2020-01-01')
# print(df)


st.write("""
# Stock Analysis App
Enter a **stock ticker** to see information about it!
""")

title = st.text_input('Stock Ticker', '')
dayz = st.text_input('History (Dayz)', '')
st.write('The current ticker title is', title)


tickerSymbol = title
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')


st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)



