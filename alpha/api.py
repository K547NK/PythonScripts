import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
#import matplotlib.pyplot as plt

keys='8C0B4ERLNTL4KOMW'

df = ForeignExchange (key=keys, output_format='pandas')
data, meta_data =df.get_currency_exchange_daily(from_symbol='USD', to_symbol='CAD',outputsize='compact')

print ('USDCAD')
print (data)
#still working out this section so its all commented out
'''
data['close'].plot()
plt.title('My First Observation')
plt.show()
'''
