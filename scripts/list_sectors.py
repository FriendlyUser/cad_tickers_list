import pandas as pd


csv_df = pd.read_csv("static/9/cse_9_2020.csv")
tsx_df = pd.read_csv("static/9/tsx_9_2020.csv")
print(csv_df.columns)
print(tsx_df.columns)

# print(csv_df[["Industry", "Identifier", "Indices"]].head())
# print(tsx_df[["sector", "peRatio", "industry"]].head())

print(list(csv_df["Industry"].unique()))
print(list(csv_df["Identifier"].unique()))

print(list(tsx_df["sector"].unique()))
print(list(tsx_df["industry"].unique()))