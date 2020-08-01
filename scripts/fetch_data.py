from cad_tickers.exchanges.tsx import dl_tsx_xlsx, add_descriptions_to_df_pp
from datetime import datetime
folder = 'static'
df = dl_tsx_xlsx()
# df = add_descriptions_to_df(df)
df = add_descriptions_to_df_pp(df)
currentMonth = datetime.now().month
currentYear = datetime.now().year
tsx_name = f"{folder}/tsx_{currentMonth}_{currentYear}.csv"
df.to_csv(tsx_name)

from cad_tickers.exchanges.cse import get_cse_tickers_df,add_descriptions_to_df
cse_df = get_cse_tickers_df()
cse_df = add_descriptions_to_df(cse_df)
cse_name = f"{folder}/cse_{currentMonth}_{currentYear}.csv"
cse_df.to_csv(cse_name)
