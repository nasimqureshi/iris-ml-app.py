import streamlit as st 
import pandas as pd
import seaborn as sn
import yfinance as yf
 
st.write("""
    # Simple Stock Price App
    Shown are the stock **closing price** and ***volume*** of Google!""")
# http://towardsdatascience.com/how-to-get-stok-data-using-python-c0de1df17e75
#define the ticker symbol.
tickerSymol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymol)
#get the historical prices fort his ticker
tickerDF= tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open High Low Close Volume Dividends Stock Splits

st.write("""
         ## Closing Price
         """)
st.line_chart(tickerDF.Close)
st.write("""
         ## Volume Price
         """)
st.line_chart(tickerDF.Volume)