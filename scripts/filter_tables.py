import dash
import dash_table
import dash_html_components as html
import pandas as pd

# 9/13/2020
# KUU MIGHT BEINSOVLENT
# Wait on BYL
# VIS.V if it makes 334,250 as projected in Q4
# PAI,Predictiv AI Inc.
# RW,RenoWorks Software Inc
# DFT,Dimension Five Technologies Inc
# KUU,Kuuhubb Inc
# BYL,Baylin Technologies Inc
# CMC,Cielo Waste Solutions Inc
# ['symbol', 'name', 'price', 'priceChange', 'percentChange',
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
tsx_df = pd.read_csv("static/9/full_9_2020.csv")
# Remove duplicates by table
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

industry = [
    "Restaurants",
    "Asset Management",
    "Forest Products",
    "Oil & Gas",
    "Industrial Products",
    "Biotechnology",
    "Farm & Heavy Construction Machinery",
    "Business Services",
    "Chemicals",
    "Medical Diagnostics & Research",
    "Metals & Mining",
    "Utilities - Independent Power Producers",
    "Retail - Defensive",
    "Utilities - Regulated",
    "REITs",
    "Banks",
    "Drug Manufacturers",
    "Aerospace & Defense",
    "Other Energy Sources",
    "Construction",
    "Hardware",
    "Real Estate",
    "Beverages - Alcoholic",
    "Retail - Cyclical",
    "Personal Services",
    "Building Materials",
    "Conglomerates",
    "Vehicles & Parts",
    "Capital Markets",
    "Manufacturing - Apparel & Accessories",
    "Travel & Leisure",
    "Healthcare Providers & Services",
    "Software",
    "Transportation",
    "Education",
    "Telecommunication Services",
    "Credit Services",
    "Consumer Packaged Goods",
    "Insurance",
    "Interactive Media",
    "Media - Diversified",
    "Industrial Distribution",
    "Agriculture",
    "Beverages - Non-Alcoholic",
    "Medical Devices & Instruments",
    "Diversified Financial Services",
    "Furnishings, Fixtures & Appliances",
    "Steel",
    "Packaging & Containers",
    "Semiconductors",
    "Waste Management",
    "Healthcare Plans",
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
            editable=True,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            columns=[{"name": i, "id": i} for i in tsx_df.columns],
            data=tsx_df.to_dict("records"),
            page_size=100,
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)