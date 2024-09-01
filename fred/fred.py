import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
fred_api_key = os.getenv('FRED_API_KEY')

# Initialize FRED API with the API key
fred = Fred(api_key=fred_api_key)

# Download GDP data from FRED
gdp_data = fred.get_series('GDP')

# Convert to DataFrame and process
gdp_df = pd.DataFrame(gdp_data, columns=['GDP'])
gdp_df.index.name = 'Date'

# Preview the data
print(gdp_df.tail())

print("\ngdp_df.info():")
gdp_df.info()

print("\ngdp_df.describe():")
gdp_df.describe()

# Handle missing values (if any)
gdp_df = gdp_df.fillna(method='ffill')

# Normalizing the data (example: min-max scaling)
gdp_df['GDP_normalized'] = (gdp_df['GDP'] - gdp_df['GDP'].min()) / (gdp_df['GDP'].max() - gdp_df['GDP'].min())

# Resampling the data to quarterly frequency
gdp_df = gdp_df.resample('Q').mean()

# Preview the processed data
print(gdp_df.head())

# Save the processed data to a CSV file
gdp_df.to_csv('processed_gdp_data.csv')