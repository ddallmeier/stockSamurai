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

tick = st.text_input('Stock Ticker', '')
st.write('The current ticker title is', tick)

tickerSymbol = tick
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

### Attempt at changing graph timeframe
# dayz = st.slider('Days', min_value=1, max_value=1000, value=5, step=1)
# # dayz = st.number_input('Insert a number')
# # st.write('The current number is ', dayz)
# stt = datetime.now()
# end = datetime.today() - timedelta(days=dayz)
# tickerDf = tickerData.history(period='1d', start=stt, end=end)

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Earnings
""")
st.line_chart(tickerDf.Earnings)





