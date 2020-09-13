from cad_tickers.exchanges.tsx import get_all_tickers_data
from datetime import datetime
import pathlib

currentMonth = datetime.now().month
folder = f"static/{currentMonth}"
pathlib.Path(folder).mkdir(parents=True, exist_ok=True)

df = get_all_tickers_data()
currentYear = datetime.now().year
tsx_name = f"{folder}/tsx_{currentMonth}_{currentYear}.csv"
df.to_csv(tsx_name, index=False)

from cad_tickers.exchanges.cse import get_cse_tickers_df, add_descriptions_to_df

cse_df = get_cse_tickers_df()
cse_df = add_descriptions_to_df(cse_df)
cse_name = f"{folder}/cse_{currentMonth}_{currentYear}.csv"
cse_df.to_csv(cse_name, index=False)
