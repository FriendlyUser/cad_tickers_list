from cad_tickers.exchanges.all_tickers import get_all_tickers_data
from datetime import datetime
import pathlib

currentMonth = datetime.now().month
folder = f"static/latest"
pathlib.Path(folder).mkdir(parents=True, exist_ok=True)

df = get_all_tickers_data()
full_name = f"{folder}/stocks.csv"
df.to_csv(full_name, index=False)
