import pandas as pd
df = pd.read_csv('full_9_2020.csv')

df.to_excel('cad_tickers.xlsx')