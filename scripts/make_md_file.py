
import pandas as pd
from datetime import datetime
from jinja2 import Template
# read the current csv into the folder
currentMonth = datetime.now().month
currentYear = datetime.now().year 
folder = f'static/{currentMonth}'
tsx_csv = f"{folder}/tsx_{currentMonth}_{currentYear}.csv"
tsx_df = pd.read_csv(tsx_csv)
tsx_json = tsx_df.to_json(orient='split')
tsx_html = tsx_df.to_html()

cse_csv = f"{folder}/cse_{currentMonth}_{currentYear}.csv"
cse_df = pd.read_csv(tsx_csv)
cse_json = cse_df.to_json(orient='split')
cse_html = cse_df.to_html()


meta = dict(
  title = f"Tickers for {currentMonth}/{currentYear}",
  position = currentMonth,
  description = f"Tickers for {currentMonth}/{currentYear}",
  version = '1.0',
  category = 'Tickers'
)

options=dict(meta=meta, cse_tickers=cse_html, tsx_tickers=tsx_html)
with open("scripts/tickers.jinja2") as file_:
  template = Template(file_.read())
tickers = template.render(**options)

md_file = f'content/en/{currentMonth}_{currentYear}.md'
with open(md_file, 'w', errors='ignore') as file_:
  file_.write(tickers)