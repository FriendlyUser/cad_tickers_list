import pickle
import requests
import os
import pathlib

folder = f"static/latest"
pathlib.Path(folder).mkdir(parents=True, exist_ok=True)


def get_tickers():
    url = os.getenv("STOCK_API")
    r = requests.get(f"{url}/api/tickers-full")
    resp = r.json()
    data = resp.get("data")
    return data


file_name = f"{folder}/tickers"
full_tickers = get_tickers()
with open("tickers", "wb") as fp:
    pickle.dump(full_tickers, fp)
