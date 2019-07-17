import csv
from mock.trading_data import *

class Trader:
    def __init__(self, purchase_amount):
        self.max_amount = 0
        self.total_amount = 0
        self.purchase_amount = purchase_amount
        self.avg_price = 0
        self.income = 0

    def deal(self, curr_price):
        if self.total_amount == 0:
            self.total_amount = self.purchase_amount / curr_price
            self.avg_price = curr_price
        elif self.avg_price < curr_price:
            self.income = self.income + (self.total_amount*curr_price - self.total_amount*self.avg_price)
            self.total_amount = 0
        else:
            curr_amount = self.purchase_amount / curr_price
            total_price = (self.total_amount*self.avg_price) + (curr_amount*curr_price)
            if total_price > self.max_amount:
                self.max_amount = total_price
            self.total_amount = self.total_amount + curr_amount
            self.avg_price = total_price / self.total_amount

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
