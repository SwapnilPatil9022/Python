import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
API_KEY = 'YOUR_API_KEY'
ticker_symbol = 'AAPL'  # Replace with the stock symbol you want to track

# Initialize Alpha Vantage API
ts = TimeSeries(key=API_KEY, output_format='pandas')
data, meta_data = ts.get_daily(symbol=ticker_symbol, outputsize='compact')

# Extract daily close prices and dates
data = data.iloc[::-1]  # Reverse DataFrame to plot in chronological order
close_prices = data['4. close']
dates = data.index

# Plotting as a bar chart
plt.figure(figsize=(10, 6))
plt.bar(dates, close_prices, color='skyblue')
plt.title(f'{ticker_symbol} Daily Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
