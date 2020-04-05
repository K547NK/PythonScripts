import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange

keys='8C0B4ERLNTL4KOMW'

df = ForeignExchange (key=keys, output_format='pandas')
ins =df.get_currency_exchange_daily(from_symbol='USD', to_symbol='CAD',outputsize='compact')

print(ins)
