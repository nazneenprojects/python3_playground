# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")



import pandas as pd

# Basic DataFrame operations
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# Reading data
print(df)

print("--------------------------------------------------------------------------------")
print(df.head(1))
print(df.tail(1))
print("------------------------------info--------------------------------------------------")
print(df.info())

print("-------------------------------describe-----------------------------------------")
print(df.describe())
print("--------------------------------------------------------------------------------")


print("--------------------------------------------------------------------------------")
df_new = pd.DataFrame({'id': [1, 2, 3, 4, 5], 'stock': ['REL', 'SAMSUNG', 'AIRTEL', 'BMW', 'KLM'], 'count': [12, 2, 5, 67, 3]})

print(df_new)

print("--------------------------------------------------------------------------------")

stocknames = df_new['stock']
print(stocknames)

stock_info = df_new[['id', 'stock']]
print(stock_info)

df_new['stock_id'] = df_new['id'] + 100

print(df_new)


df_filter = df[df_new['id'] < 400]
print(df_filter)

average_stock = df_new['count'].mean()
print(average_stock)
max_count = df_new['count'].max()
print(max_count)


print(df_new.sort_values('count', ascending=False))

