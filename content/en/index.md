---
title: Introduction
description: 'Explains what the project does'
position: 1
category: Getting started
version: 1.4
fullscreen: false
---

<alert type="info">

This project is meant to automatically track all tickers from the cse, tsx and tsxv exchanges. 

</alert>

Eventually, it will cover all the exchanges if I get to updating my original package updated for all exchanges [cad-tickers](https://pypi.org/project/cad-tickers/).

Outputting python script with detailed descriptions.

<code-group>
  <code-block label="Python" active>

  ```python
    from cad_tickers.exchanges.tsx import dl_tsx_xlsx, add_descriptions_to_df_pp
    from datetime import datetime
    import pathlib
    currentMonth = datetime.now().month
    folder = f'static/{currentMonth}'
    pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
    df = dl_tsx_xlsx()
    df = add_descriptions_to_df_pp(df)
    currentYear = datetime.now().year
    tsx_name = f"{folder}/tsx_{currentMonth}_{currentYear}.csv"
    df.to_csv(tsx_name)
    from cad_tickers.exchanges.cse import get_cse_tickers_df,add_descriptions_to_df
    cse_df = get_cse_tickers_df()
    cse_df = add_descriptions_to_df(cse_df)
    cse_name = f"{folder}/cse_{currentMonth}_{currentYear}.csv"
    cse_df.to_csv(cse_name)
  ```
  </code-block>
</code-group>


Script to output json and html data.


<code-group>
  <code-block label="Python" active>

  ```python
    import pandas as pd
    from datetime import datetime
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
  ```
  </code-block>
</code-group>
