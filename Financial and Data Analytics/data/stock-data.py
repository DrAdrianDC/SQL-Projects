# Stock data from yfinance library

# Import libraries
import yfinance as yf
import pandas as pd


# Download data
spy500 = yf.download("SPY", start="2011-01-01", end="2024-12-20")

# Save the downloaded data to a CSV file
spy500.to_csv('spy500_data.csv', index=True)  # Save with the index as the Date column

# Error Handling for empty data
if spy500.empty:
    print("Failed to download data. Please check the ticker or internet connection.")
    exit()

# Handle MultiIndex: Extract 'Close' for 'SPY'
if ('Close', 'SPY') not in spy500.columns:
    print("Error: ('Close', 'SPY') column not found in the data.")
    exit()

# Extract and preprocess 'Close' prices
dataset_spy500 = spy500[('Close', 'SPY')].copy()
dataset_spy500.name = 'Close'  # Rename for clarity
dataset_spy500 = dataset_spy500.dropna()

# Add dates as the index
dataset_spy500 = dataset_spy500.reset_index()
dataset_spy500['Date'] = pd.to_datetime(dataset_spy500['Date'])  # Ensure proper datetime format
dataset_spy500.set_index('Date', inplace=True)
