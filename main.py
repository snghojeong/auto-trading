import csv
from mock.trading_data import *

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
    for record in cooked:
        cnt = cnt + 1
        curr_ts = int(record[idx_ts]);
        if (curr_ts - last_ts) > (60 * 60 * 24):
            last_ts = curr_ts
            curr_price = float(record[idx_pr])
            if total_amount == 0:
                total_amount = purchase_amount / curr_price
                avg_price = curr_price
            elif avg_price < curr_price:
                income = income + (total_amount*curr_price - total_amount*avg_price)
                total_amount = 0
            else:
                curr_amount = purchase_amount / curr_price
                total_price = (total_amount*avg_price) + (curr_amount*curr_price)
                if total_price > max_funds:
                    max_funds = total_price
                total_amount = total_amount + curr_amount
                avg_price = total_price / total_amount
            print('Count: ', cnt, '\tMAX asset: ', max_funds, '\tIncome: ', income, end='\r')
    print('\nCount: ', cnt, '\tMAX asset: ', max_funds, '\tIncome: ', income, '\tCurrent asset: ', total_amount * avg_price)
