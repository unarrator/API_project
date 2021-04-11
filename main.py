import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of ANY STOCK!
""")


tickerSymbol = st.text_input('Input your tickersymbol here:')
st.write('#Or')

tickerSymbol = st.selectbox(
    'TOP STOCKS',
     ('GOOGL', 'AAPL', 'FB', 'TSLA', 'MSFT'))

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)