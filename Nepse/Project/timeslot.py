import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Nabil Bank.csv')
total_data =  len(df)
print(f' Total no of rows {total_data}')

data = df.iloc[::-1].reset_index(drop=True)


window_size = 120
sliding_size = 30


for i in range(0, total_data - window_size+1, sliding_size ):
    window_data = data.iloc[i:i + window_size]

    plt.figure(figsize=(12, 6))
    plt.plot(window_data['Date'], window_data['Close'], label=f'Close Price (Window {i // sliding_size + 1})')
    plt.xticks([0, len(window_data) - 1], [window_data['Date'].iloc[0], window_data['Date'].iloc[-1]], rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title(f'Close Price History - Window {i // sliding_size + 1}')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

    close_prices = window_data['Close'].values
    VG = ts2vg.NaturalVG(directed = None)
    VG.build(close_prices)

    nxg = VG.as_networkx()

    plt.figure(figsize=(8, 6))
    pos = VG.node_positions()
    nx.draw_networkx(nxg, pos=pos, node_size=50, node_color="blue", edge_color="gray", with_labels=False)
    plt.title(f'Visibility Graph for window {i} to {i + window_size}')
    plt.show()