import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create sample stock data
dates = pd.date_range(start='2024-01-01', end='2024-01-31')
np.random.seed(42)  # For reproducible results

data = {
    'Date': dates,
    'Open': np.random.uniform(100, 110, len(dates)),
    'High': np.random.uniform(110, 120, len(dates)),
    'Low': np.random.uniform(90, 100, len(dates)),
    'Close': np.random.uniform(100, 110, len(dates)),
    'Volume': np.random.randint(10000, 100000, len(dates)),
    'Symbol': 'AAPL',
    # Adding some missing values and errors for cleaning exercise
    'Price_Category': ['High', 'Low', 'Medium', None, 'High', 'Low', None] * 5,
}

df = pd.DataFrame(data)
df.to_csv('stock_data.csv', index=False)
