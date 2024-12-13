import pandas as pd

df = pd.read_csv('results.csv')

opening = df['today opening'][:6].to_numpy()
closing = df['yesterday closing'][1:].to_numpy()

print(opening)
print(closing)

net_change = closing - opening

print(net_change)