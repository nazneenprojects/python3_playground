import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({
    'stock': ['AAPL', 'GOOGL', 'MSFT'],
    'price': [150, 2800, 300]
})

df2 = pd.DataFrame({
    'stock': ['AAPL', 'GOOGL', 'META'],
    'volume': [1000, 500, 750]
})



# Merge 
merged = pd.merge(df1, df2, on='stock', how='inner')
merged_outer = pd.merge(df1, df2, on='stock', how='outer')
print("Merged: \n", merged)
print("merged_outer: \n", merged_outer)


# Concatenation
combined = pd.concat([df1, df2], axis=0)  # Vertical
combined_horizontal = pd.concat([df1, df2], axis=1)  # Horizontal

print("-------------------------------------------")
print(combined)
print("-------------------------------------------")
print(combined_horizontal)


# create time series data
dates = pd.date_range('2024-01-01', '2024-01-10')#

ts_data = pd.DataFrame({
    'date': dates,
    'price': [100, 102, 101, 103, 105, 104, 107, 106, 108, 110]
    
})


ts_data.set_index('date', inplace=True)

print(ts_data)


weekly_avg = ts_data.resample('W').mean()
print(weekly_avg)



# Rolling windows (Moving averages)
ts_data['MA5'] = ts_data['price'].rolling(window=5).mean()

print(ts_data['MA5'] )

# Shifting data (for calculating returns)
ts_data['prev_price'] = ts_data['price'].shift(1)
ts_data['returns'] = (ts_data['price'] - ts_data['prev_price']) / ts_data['prev_price']

print(ts_data['prev_price'])
print(ts_data['returns'])


# Pivot tables
pivot_table = df.pivot_table(
    values='price',
    index='date',
    columns='stock',
    aggfunc='mean'
)

# Melt (unpivot)
melted = pivot_table.melt(ignore_index=False)

# Apply custom functions
def calculate_metric(x):
    return (x - x.mean()) / x.std()

ts_data['normalized'] = ts_data['price'].apply(calculate_metric)


# Calculate daily returns
returns = ts_data['price'].pct_change()

# Calculate volatility
volatility = returns.rolling(window=20).std() * (252 ** 0.5)  # Annualized

# Calculate OHLC from tick data
ohlc = tick_data.resample('D').agg({
    'price': ['first', 'max', 'min', 'last'],
    'volume': 'sum'
}).rename(columns={
    'first': 'open',
    'max': 'high',
    'min': 'low',
    'last': 'close'
})


# Vectorized operations (faster than loops)
returns = np.log(df['price'] / df['price'].shift(1))

# Efficient data type usage
df['category'] = df['category'].astype('category')

# Using query() for filtering
result = df.query('price > 100 and volume > 1000')
