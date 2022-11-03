import yfinance as yf
df = yf.download('AAPL', start='2019-01-01', end='2020-01-01')
print(df)