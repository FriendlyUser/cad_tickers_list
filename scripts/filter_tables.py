import dash
import dash_table
import dash_html_components as html
import pandas as pd

# ['Unnamed: 0', 'symbol', 'name', 'price', 'priceChange', 'percentChange',
#  'exchangeName', 'exShortName', 'exchangeCode', 'marketPlace', 'sector',
#  'industry', 'volume', 'openPrice', 'dayHigh', 'dayLow', 'MarketCap',
#  'MarketCapAllClasses', 'peRatio', 'prevClose', 'dividendFrequency',
#  'dividendYield', 'dividendAmount', 'dividendCurrency', 'beta', 'eps',
#  'exDividendDate', 'shortDescription', 'longDescription', 'website',
#  'email', 'phoneNumber', 'fullAddress', 'employees', 'shareOutStanding',
#  'totalDebtToEquity', 'totalSharesOutStanding', 'sharesESCROW', 'vwap',
#  'dividendPayDate', 'weeks52high', 'weeks52low', 'alpha',
#  'averageVolume10D', 'averageVolume30D', 'averageVolume50D',
#  'priceToBook', 'priceToCashFlow', 'returnOnEquity', 'returnOnAssets',
#  'day21MovingAvg', 'day50MovingAvg', 'day200MovingAvg', 'dividend3Years',
#  'dividend5Years', 'datatype', '__typename']
tsx_df = pd.read_csv("static/9/tsx_9_2020.csv")
tsx_df = tsx_df[
    [
        "symbol",
        "price",
        "volume",
        "sector",
        "industry",
        "peRatio",
        "shortDescription",
    ]
]
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        dash_table.DataTable(
            id="table",
            style_cell={
                "whiteSpace": "normal",
                "height": "auto",
            },
            columns=[{"name": i, "id": i} for i in tsx_df.columns],
            data=tsx_df.to_dict("records"),
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)