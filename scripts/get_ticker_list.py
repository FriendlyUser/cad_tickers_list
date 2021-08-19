import pickle
import requests
import os
import pathlib
import json
from cad_tickers.exchanges.cse import get_cse_tickers_df

folder = f"static/latest"
pathlib.Path(folder).mkdir(parents=True, exist_ok=True)


def get_tickers():
    url = os.getenv("STOCK_API")
    r = requests.get(f"{url}/api/tickers-full")
    resp = r.json()
    data = resp.get("data")
    return data

file_name = f"{folder}/tickers"
raw_file_name = f"{folder}/raw_tickers.json"
full_tickers = get_tickers()
with open(file_name, "wb") as fp:
    pickle.dump(full_tickers, fp)

with open(raw_file_name, 'w', encoding='utf-8') as f:
    json.dump(full_tickers, f, ensure_ascii=False, indent=4)
    

cse_df = get_cse_tickers_df()
cse_path = f"{folder}/cse.csv"
cse_df.to_csv(cse_path,index=False)