import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
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
tsx_df = pd.read_csv(
    "https://raw.githubusercontent.com/FriendlyUser/cad_tickers_list/main/static/latest/stocks.csv"
)
# Remove duplicates by table
tsx_df = tsx_df[
    [
        "symbol",
        "price",
        "volume",
        "sector",
        "exchangeCode",
        "returnOnEquity",
        "returnOnAssets",
        "alpha",
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

st.write(tsx_df)
