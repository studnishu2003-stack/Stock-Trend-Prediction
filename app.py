pip install pandas_datareader
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
pip install keras
pip install yfinance
from keras.models import 

import yfinance as yf
import pandas as pd

# Define the date range
start = '2010-01-01'
end = '2025-07-31'
st.title('Stock Trend Prediction')

user_input = st.text_input('Enter Stock Ticker','AAPL')

# Get Apple stock data using yfinance instead of data.DataReader
df = yf.download('AAPL', start=start, end=end)
# Describing the data
st.subheader('Data from 2010-2025')
st.write(df.describe())

# Display the first few rows
df.head()




