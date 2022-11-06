import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import steamlit as st
import pandas as pd

## Data selection 
df = yf.download('AAPL', start='2019-01-01', end='2020-01-01')
print(df)












