import csv
from traders import *

fd_pos_max_price = 213605280
one_day = 60 * 60 * 24

idx_ts = 0
idx_pr = 1
idx_am = 2

with open('./korbitKRW.csv', 'r') as raw:
    raw.seek(fd_pos_max_price)
    cooked = csv.reader(raw)
    cnt = 0
    last_ts = 0
    start_ts = 0
    traders = [ SimpleTrader(10000), StepTrader(10000), StepExpTrader(10000) ]
    for record in cooked:
        cnt = cnt + 1
        curr_ts = int(record[idx_ts]);
        if (curr_ts - last_ts) > one_day:
            last_ts = curr_ts
            print('Count: {0:8d}'.format(cnt), end=', ')
            for trader in traders:
                trader.deal(float(record[idx_pr]))
                print('[ {0}, MAX asset: {1:10.0f}, Income: {2:8.0f} ]'.format(trader.name, trader.max_amount, trader.income), end=', ')
            print('TS: ', curr_ts, end='\r')
            if start_ts == 0:
                start_ts = curr_ts
    elasped_year = (curr_ts - start_ts)/one_day/365
    print('End of simulation')
    print('Count: {0:8d}'.format(cnt))
    for trader in traders:
        print('MAX asset: {0:10.0f}, Income: {1:8.0f}'.format(trader.max_amount, trader.income))
        print('Ratio: ', trader.income*100/trader.max_amount/elasped_year)
        trader.print_asset();
