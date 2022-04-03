from cad_tickers.exchanges.all_tickers import mk_full_tickers
from datetime import datetime
import pathlib

currentMonth = datetime.now().month
folder = f"static/latest"
pathlib.Path(folder).mkdir(parents=True, exist_ok=True)

df = mk_full_tickers()
df.drop_duplicates(subset="symbol", keep="first", inplace=True)
full_name = f"{folder}/stocks.csv"
df.to_csv(full_name, index=False)
