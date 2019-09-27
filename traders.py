class SimpleTrader:
    def __init__(self, purchase_amount):
        self.max_amount = 0
        self.total_amount = 0
        self.acc_price = 0
        self.deal_cnt = 0
        self.purchase_amount = purchase_amount
        self.avg_price = 0
        self.income = 0
        self.name = 'SimpleTrader'

    def deal(self, curr_price):
        self.deal_cnt = self.deal_cnt + 1
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
        self.acc_price = self.acc_price + (self.avg_price * self.total_amount)

    def print_asset(self):
        print('----------')
        print('price: ', self.avg_price)
        print('amount: ', self.total_amount, ', ', self.acc_price)
        print('total: ', self.avg_price*self.total_amount)
        print('----------')

class Asset:
    def __init__(self):
        self.price = 0
        self.amount = 0

class StepTrader:
    def __init__(self, purchase_amount):
        self.asset_list = []
        self.income = 0
        self.purchase_amount = purchase_amount
        self.max_amount = 0
        self.total_amount = 0
        self.acc_price = 0
        self.deal_cnt = 0
        self.avg_price = 0
        self.name = 'StepTrader'

    def deal(self, curr_price):
        self.deal_cnt = self.deal_cnt + 1
        for asset in list(filter(lambda x: x.price < curr_price, self.asset_list)):
            self.income = self.income + (curr_price - asset.price)*asset.amount
        self.asset_list = list(filter(lambda x: x.price >= curr_price, self.asset_list))
        item = Asset()
        item.price = curr_price
        item.amount = self.purchase_amount / curr_price
        self.asset_list.append(item)
        total_price = 0
        for asset in self.asset_list:
            total_price = total_price + (asset.price * asset.amount)
        self.total_amount = total_price
        if self.max_amount < total_price:
            self.max_amount = total_price
        self.acc_price = self.acc_price + (self.avg_price * self.total_amount)

    def print_asset(self):
        total_amount = 0
        total_price = 0
        for asset in self.asset_list:
            print('----------')
            print('price: ', asset.price)
            print('amount: ', asset.amount)
            print('total: ', asset.price * asset.amount)
            total_amount = total_amount + asset.amount
            total_price = total_price + (asset.price*asset.amount)
        print('----------')
        print('Average price: ', )

class StepExpTrader:
    def __init__(self, purchase_amount):
        self.asset_list = []
        self.income = 0
        self.purchase_amount = purchase_amount
        self.max_amount = 0
        self.total_amount = 0
        self.avg_price = 0
        self.name = 'StepExpTrader'
        self.acc_price = 0
        self.deal_cnt = 0

    def deal(self, curr_price):
        self.deal_cnt = self.deal_cnt + 1
        for asset in list(filter(lambda x: x.price < curr_price, self.asset_list)):
            self.income = self.income + (curr_price - asset.price)*asset.amount
        self.asset_list = list(filter(lambda x: x.price >= curr_price, self.asset_list))
        curr_amount = self.purchase_amount / curr_price
        for asset in self.asset_list:
            asset.price = ((asset.price * asset.amount) + (curr_price * curr_amount)) / (asset.amount + curr_amount)
            asset.amount = asset.amount + curr_amount
        item = Asset()
        item.price = curr_price
        item.amount = curr_amount
        self.asset_list.append(item)
        total_price = 0
        for asset in self.asset_list:
            total_price = total_price + (asset.price * asset.amount)
        self.total_amount = total_price
        if self.max_amount < total_price:
            self.max_amount = total_price
        self.acc_price = self.acc_price + (self.avg_price * self.total_amount)

    def print_asset(self):
        total_amount = 0
        total_price = 0
        for asset in self.asset_list:
            print('----------')
            print('price: ', asset.price)
            print('amount: ', asset.amount)
            print('total: ', asset.price * asset.amount)
            total_amount = total_amount + asset.amount
            total_price = total_price + (asset.price*asset.amount)
        print('----------')
        print('Average price: ', )

class PessimisticTrader:
    def __init__(self, purchase_amount):
        self.max_amount = 0
        self.total_amount = 0
        self.purchase_amount = purchase_amount
        self.avg_price = 0
        self.income = 0
        self.pass_cnt = 0
        self.max_pass_cnt = 0
        self.name = 'PessimisticTrader'
        self.acc_price = 0
        self.deal_cnt = 0

    def deal(self, curr_price):
        self.deal_cnt = self.deal_cnt + 1
        if self.total_amount == 0:
            self.total_amount = self.purchase_amount / curr_price
            self.avg_price = curr_price
        elif self.avg_price < curr_price:
            self.income = self.income + (self.total_amount*curr_price - self.total_amount*self.avg_price)
            self.total_amount = 0
        else:
            if self.pass_cnt >= self.max_pass_cnt:
                self.max_pass_cnt = self.max_pass_cnt + 1
                self.pass_cnt = 0;
                curr_amount = self.purchase_amount / curr_price
                total_price = (self.total_amount*self.avg_price) + (curr_amount*curr_price)
                if total_price > self.max_amount:
                    self.max_amount = total_price
                self.total_amount = self.total_amount + curr_amount
                self.avg_price = total_price / self.total_amount
            else:
                self.pass_cnt = self.pass_cnt + 1;
        self.acc_price = self.acc_price + (self.avg_price * self.total_amount)

    def print_asset(self):
        print('----------')
        print('price: ', self.avg_price)
        print('amount: ', self.total_amount)
        print('total: ', self.avg_price*self.total_amount)
        print('----------')

class ExponentialAggressiveTrader:
    def __init__(self, purchase_amount):
        self.max_amount = 0
        self.total_amount = 0
        self.purchase_amount = purchase_amount
        self.curr_purchase = self.purchase_amount;
        self.avg_price = 0
        self.income = 0
        self.name = 'ExponentialAggressiveTrader'
        self.acc_price = 0
        self.deal_cnt = 0

    def deal(self, curr_price):
        self.deal_cnt = self.deal_cnt + 1
        if self.total_amount == 0:
            self.total_amount = self.curr_purchase / curr_price
            self.curr_purchase = self.curr_purchase * 2
            self.avg_price = curr_price
        elif self.avg_price < curr_price:
            self.income = self.income + (self.total_amount*curr_price - self.total_amount*self.avg_price)
            self.total_amount = 0
            self.curr_purchase = self.purchase_amount
        else:
            curr_amount = self.curr_purchase / curr_price
            self.curr_purchase = self.curr_purchase * 2
            total_price = (self.total_amount*self.avg_price) + (curr_amount*curr_price)
            if total_price > self.max_amount:
                self.max_amount = total_price
            self.total_amount = self.total_amount + curr_amount
            self.avg_price = total_price / self.total_amount
        self.acc_price = self.acc_price + (self.avg_price * self.total_amount)

    def print_asset(self):
        print('----------')
        print('price: ', self.avg_price)
        print('amount: ', self.total_amount)
        print('total: ', self.avg_price*self.total_amount)
        print('----------')

class LinearAggressiveTrader:
    def __init__(self, purchase_amount):
        self.max_amount = 0
        self.total_amount = 0
        self.purchase_amount = purchase_amount
        self.curr_purchase = self.purchase_amount;
        self.avg_price = 0
        self.income = 0
        self.name = 'LinearAggressiveTrader'
        self.acc_price = 0
        self.deal_cnt = 0

    def deal(self, curr_price):
        self.deal_cnt = self.deal_cnt + 1
        if self.total_amount == 0:
            self.total_amount = self.curr_purchase / curr_price
            self.curr_purchase = self.curr_purchase * 2
            self.avg_price = curr_price
        elif self.avg_price < curr_price:
            self.income = self.income + (self.total_amount*curr_price - self.total_amount*self.avg_price)
            self.total_amount = 0
            self.curr_purchase = self.purchase_amount
        else:
            curr_amount = self.curr_purchase / curr_price
            self.curr_purchase = self.curr_purchase + self.purchase_amount
            total_price = (self.total_amount*self.avg_price) + (curr_amount*curr_price)
            if total_price > self.max_amount:
                self.max_amount = total_price
            self.total_amount = self.total_amount + curr_amount
            self.avg_price = total_price / self.total_amount
        self.acc_price = self.acc_price + (self.avg_price * self.total_amount)

    def print_asset(self):
        print('----------')
        print('price: ', self.avg_price)
        print('amount: ', self.total_amount)
        print('total: ', self.avg_price*self.total_amount)
        print('----------')


