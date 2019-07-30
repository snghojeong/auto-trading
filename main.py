import csv
from mock.trading_data import *
from traders import *

idx_ts = 0
idx_pr = 1
idx_am = 2

purchase_amount = 100000
income = 0
max_funds = 0
avg_price = 0
total_amount = 0
asset_list = []

with open('./korbitKRW.csv', 'r') as raw:
    cooked = csv.reader(raw)
    cnt = 0
    last_ts = 0
    trader = Trader(10000)
    for record in cooked:
        cnt = cnt + 1
        curr_ts = int(record[idx_ts]);
        if (curr_ts - last_ts) > (60 * 60 * 24):
            last_ts = curr_ts
            trader.deal(float(record[idx_pr]))
            print('Count: ', cnt, '\tMAX asset: ', trader.max_amount, '\tIncome: ', trader.income, end='\r')
    print('\nCount: ', cnt, '\tMAX asset: ', trader.max_amount, '\tIncome: ', trader.income, '\tCurrent asset: ', trader.total_amount * trader.avg_price)
