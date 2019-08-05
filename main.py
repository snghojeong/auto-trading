import csv
from mock.trading_data import *
from traders import *

pre_max = 4532075 # the index of previous highest price of BTC

idx_ts = 0
idx_pr = 1
idx_am = 2

with open('./korbitKRW.csv', 'r') as raw:
    cooked = csv.reader(raw)
    cnt = 0
    last_ts = 0
    trader = SimpleTrader(10000)
    for record in cooked:
        cnt = cnt + 1
        curr_ts = int(record[idx_ts]);
        print('Count: ', cnt, end='\r')
        if (cnt > pre_max):
            if (curr_ts - last_ts) > (60 * 60 * 24):
                last_ts = curr_ts
                trader.deal(float(record[idx_pr]))
                print('Count: ', cnt, '\tMAX asset: ', trader.max_amount, '\tIncome: ', trader.income, end='\r')
    print('\nCount: ', cnt, '\tMAX asset: ', trader.max_amount, '\tIncome: ', trader.income, '\tRatio: ', trader.income*100/trader.max_amount, '\tCurrent asset: ', trader.total_amount * trader.avg_price)
