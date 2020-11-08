
import pandas as pd
from datetime import datetime
from jinja2 import Template
# read the current csv into the folder
currentMonth = datetime.now().month
currentYear = datetime.now().year 
folder = f'static/{currentMonth}'

# TODO fix later
# Streamlit site is a much better idea

# tsx_csv = f"{folder}/tsx_{currentMonth}_{currentYear}.csv"
# tsx_df = pd.read_csv(tsx_csv)
# # drop undesired rows
# tsx_df = tsx_df.drop(['Unnamed: 0', 'QMV($)','HQ Region'],axis=1, errors='ignore')
# tsx_json = tsx_df.to_json(orient='split')
# tsx_html = tsx_df.to_html(index=False,index_names=False, show_dimensions=True)

# cse_csv = f"{folder}/cse_{currentMonth}_{currentYear}.csv"
# cse_df = pd.read_csv(cse_csv)
# cse_df = cse_df.drop(['Unnamed: 0', 'Currency','urls'],axis=1, errors='ignore')
# cse_json = cse_df.to_json(orient='split')
# cse_html = cse_df.to_html(index=False,index_names=False, show_dimensions=True)

# meta = dict(
#   title = f"Tickers for {currentMonth}/{currentYear}",
#   position = currentMonth,
#   description = f"Tickers for {currentMonth}/{currentYear}",
#   version = '1.0',
#   category = 'Tickers'
# )

# options=dict(meta=meta, cse_tickers=cse_html, tsx_tickers=tsx_html)
# with open("scripts/tickers.jinja2") as file_:
#   template = Template(file_.read())
# tickers = template.render(**options)

# md_file = f'content/en/{currentMonth}_{currentYear}.md'
# with open(md_file, 'w', errors='ignore') as file_:
#   file_.write(tickers)