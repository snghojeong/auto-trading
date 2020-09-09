from pandas_datareader import data
from matplotlib import pyplot as plt
import math
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

def simulate(cash, data):
    asset = 0
    result = list() 
    for key in data['Open'].keys():
        cash = cash + (asset * data['Open'][key])

        asset = math.floor(cash / data['Close'][key])
        cash = cash - (asset * data['Close'][key])
        cash = cash + (asset * data['Open'][key])
        result.append(cash)

        asset = math.floor(cash / data['Close'][key])
        cash = cash - (asset * data['Close'][key])
    return result

kospi = data.DataReader('^KS11', 'yahoo', start='1900-01-01')
print(kospi['Close'])
kosdaq = data.DataReader('^KQ11', 'yahoo', start='1900-01-01')
print(kosdaq['Close'])

kospi_result = simulate(10000000, kospi) 
kosdaq_result = simulate(10000000, kosdaq) 

plt.subplot(2,1,1)
plt.plot(kospi_result, label='KOSPI')
plt.subplot(2,1,2)
plt.plot(kosdaq_result, label='KOSDAQ')
plt.show()
