class SimpleTrader:
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

    def print_asset(self):
        print('----------')
        print('price: ', self.avg_price)
        print('amount: ', self.total_amount)
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
        self.avg_price = 0

    def deal(self, curr_price):
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

    def print_asset(self):
        total_amount = 0
        total_price = 0
        for asset in self.asset_list:
            print('----------')
            print('price: ', asset.price)
            print('amount: ', asset.amount)
            total_amount = total_amount + asset.amount
            total_price = total_price + (asset.price*asset.amount)
        print('----------')
        print('Average price: ', )
