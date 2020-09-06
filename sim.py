from pandas_datareader import data
from matplotlib import pyplot as plt
import math

kospi = data.DataReader('^KS11', 'yahoo')
# kosdaq = data.DataReader('KQ11', 'yahoo')

cash = 10000000
asset = 0
tracking = []
for oprice, cprice in zip(kospi['Open'], kospi['Close']):
    cash = cash + (asset * oprice)
    tracking.append(cash)
    asset = math.floor(cash / cprice)
    cash = cash - (asset * cprice)

plt.subplot(1,1,1)
plt.plot(tracking, label='Stock ratio')
plt.show()
