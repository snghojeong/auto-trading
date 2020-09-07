from pandas_datareader import data
from matplotlib import pyplot as plt
import math
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

kospi = data.DataReader('^KS11', 'yahoo', start='1900-01-01')
# kosdaq = data.DataReader('KQ11', 'yahoo')

cash = 10000000
asset = 0
tracking = list() 
print(kospi['Close'])
for key in kospi['Open'].keys():
    cash = cash + (asset * kospi['Open'][key])
    tracking.append(cash)
    asset = math.floor(cash / kospi['Close'][key])
    cash = cash - (asset * kospi['Close'][key])

plt.subplot(2,1,1)
plt.plot(tracking, label='1')
plt.subplot(2,1,2)
plt.plot(tracking, label='2')
plt.show()
