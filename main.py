import csv
from traders import *

fd_pos_max_price = 213605280
one_day = 60 * 60 * 24

idx_ts = 0
idx_pr = 1
idx_am = 2

def getoutrow(ts, price, traders):
    output = list()
    output.append(ts)
    output.append(price)
    output.append(traders[0].income)
    output.append(traders[1].income)
    output.append(traders[2].income)
    output.append(traders[3].income)
    return output

with open('./korbitKRW.csv', 'r') as raw, open('./output.csv', 'w') as outfile:
    raw.seek(fd_pos_max_price)
    cooked = csv.reader(raw)
    outwriter = csv.writer(outfile)
    cnt = 0
    last_ts = 0
    start_ts = 0
    traders = [ SimpleTrader(10000), PessimisticTrader(10000), ExponentialAggressiveTrader(10000), LinearAggressiveTrader(10000), RebalancingTrader(10000) ]
    for record in cooked:
        cnt = cnt + 1
        curr_ts = int(record[idx_ts]);
        if (curr_ts - last_ts) > one_day:
            last_ts = curr_ts
            print('Count: {0:8d}'.format(cnt), end=', ')
            for trader in traders:
                trader.deal(float(record[idx_pr]))
                print('[ {0}, MAX asset: {1:10.0f}, Income: {2:8.0f} ]'.format(trader.name, trader.max_amount, trader.income), end=', ')
            print('TS: ', curr_ts)
            outwriter.writerow(getoutrow(curr_ts, float(record[idx_pr]), traders))
            if start_ts == 0:
                start_ts = curr_ts
    elasped_year = (curr_ts - start_ts)/one_day/365
    print('End of simulation')
    print('Count: {0:8d}'.format(cnt))
    for trader in traders:
        trader.print_asset();
        print('=========================')
        print('Name: ', trader.name)
        print('Income: {1:8.0f}, MAX asset: {0:10.0f}, AVG asset: {2:10.0f}'.format(trader.max_amount, trader.income, trader.acc_price/trader.deal_cnt))
        print('Ratio: ', trader.income*100/trader.max_amount/elasped_year, ', ', trader.income*100/(trader.acc_price/trader.deal_cnt)/elasped_year)
        print('=========================')
