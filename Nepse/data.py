import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('SICL data.csv')

print(df.info())

print(df.head(20))

plt.figure(figsize=(12,6))
plt.plot(df.Date, df.Close, label='Close Price history')
plt.title(f'Close Price History of {df.Symbol}')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.show()

