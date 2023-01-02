import pandas as pd
from helpers import retrieve_company_code
from exceptions import NoAvailableData
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
from pandas_datareader import data as pdr
import yfinance as yfin

yfin.pdr_override()

companies_df = pd.read_csv("static/companiesCodes.csv")

# Must be passed from the web app
company_name = "Google"

# Select all codes that cointain the company name
codes_df = retrieve_company_code(companies_df, company_name)

# TODO
# Pick the first of the selected codes
company_code = codes_df.iloc[2]["YAHOO TICKER"]

# Six months of data
start_date = dt.today() + relativedelta(months=-6)
end_date = dt.today()

data_df = pdr.get_data_yahoo(company_code, start = start_date, end = end_date, auto_adjust=True)

data_df.columns = data_df.columns.map(''.join)
data_df['day_of_month'] = data_df.index.day
data_df['day_of_week'] = data_df.index.dayofweek
data_df['month'] = data_df.index.month

# Divide data into train and test
data_len = len(data_df)
train_size = int(data_len * 0.9)
test_size = data_len - train_size
train, test = data_df.iloc[0:train_size], data_df.iloc[train_size:data_len]

