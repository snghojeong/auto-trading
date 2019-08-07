import csv
from traders import *

pre_max = 4532075 # the index of previous highest price of BTC
one_day = 60 * 60 * 24

idx_ts = 0
idx_pr = 1
idx_am = 2

with open('./korbitKRW.csv', 'r') as raw:
    cooked = csv.reader(raw)
    cnt = 0
    last_ts = 0
    traders = [ SimpleTrader(10000), StepTrader(10000) ]
    for record in cooked:
        cnt = cnt + 1
        curr_ts = int(record[idx_ts]);
        print('Count: {0:8d}'.format(cnt), end='\r')
        if (cnt > pre_max):
            if (curr_ts - last_ts) > one_day:
                last_ts = curr_ts
                print('Count: {0:8d}'.format(cnt), end=', ')
                for trader in traders:
                    trader.deal(float(record[idx_pr]))
                    print('[ MAX asset: {0:10.0f}, Income: {1:8.0f} ]'.format(trader.max_amount, trader.income), end=', ')
                print('TS: ', curr_ts, end='\r')
    for trader in traders:
        print('Count: ', cnt, '\tMAX asset: ', trader.max_amount, '\tIncome: ', trader.income, '\tRatio: ', trader.income*100/trader.max_amount)
        trader.print_asset();
