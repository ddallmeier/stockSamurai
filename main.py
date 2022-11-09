import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import streamlit as st
import pandas as pd
import numpy as np
from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator
import seaborn as sns

###########
# sidebar #
###########
option = st.sidebar.text_input('Stock Ticker', 'msft')
import datetime
today = datetime.date.today()
before = today - datetime.timedelta(days=700)
start_date = st.sidebar.date_input('Start date', before)
end_date = st.sidebar.date_input('End date', today)
if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.sidebar.error('Error: End date must fall after start date.')

##############
# Stock data #
##############

# Download data
df = yf.download(option,start= start_date,end= end_date, progress=False)

# Plot green factors
## TODO Add divergence from mean/median

def sustainability(ticker):
    env = yf.Ticker(ticker).sustainability
    env = env.iloc[-3].Value
    return env

def total_esg(ticker):
    env = yf.Ticker(ticker).sustainability
    env = env.iloc[-12].Value
    return env

def percentilez(ticker):
    env = yf.Ticker(ticker).sustainability
    env = env.iloc[-6].Value
    return env

green = sustainability(option)
total_ = total_esg(option)
percentile_ = percentilez(option)

# st.metric(label="Environment Score", value=green, delta=0.0)

col1, col2, col3 = st.columns(3)
col1.metric("Environment Score", green, 0.0)
col2.metric("Total ESG",total_ , 0.0)
col3.metric("Percentile",percentile_ , 0.0)


# Bollinger Bands
indicator_bb = BollingerBands(df['Close'])
bb = df
bb['bb_h'] = indicator_bb.bollinger_hband()
bb['bb_l'] = indicator_bb.bollinger_lband()
bb = bb[['Close','bb_h','bb_l']]


# Revenue
def get_earnings(ticker):
    earn = yf.Ticker(ticker).earnings
    return earn
rev = get_earnings(option)

###################
# Set up main app #
###################

# Plot the prices and the bolinger bands
st.write('Stock Bollinger Bands')
st.line_chart(bb)

# Plot Revenue
st.write('Revenue of ',option, 'is: ')
st.line_chart(rev)


# Display Reccomendations
## TODO CONDIITONAL formatting
def get_recommendations(ticker):
    rec = yf.Ticker(ticker).recommendations
    return rec
rec = get_recommendations(option)

st.markdown('<p style="font-family:sans-serif; color:Green; font-size: 42px;">Reccomendations</p>', unsafe_allow_html=True)
st.dataframe(rec, use_container_width=True)


















# Download Data Button
# def to_excel(df):
#     output = BytesIO()
#     writer = pd.ExcelWriter(output, engine='xlsxwriter')
#     df.to_excel(writer, sheet_name='Sheet1')
#     writer.save()
#     processed_data = output.getvalue()
#     return processed_data

# def get_table_download_link(df):
#     """Generates a link allowing the data in a given panda dataframe to be downloaded
#     in:  dataframe
#     out: href string
#     """
#     val = to_excel(df)
#     b64 = base64.b64encode(val)  # val looks like b'...'
#     return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="download.xlsx">Download excel file</a>' # decode b'abc' => abc

# st.markdown(get_table_download_link(df), unsafe_allow_html=True)
