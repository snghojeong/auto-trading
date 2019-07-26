class Trader:
    def __init__(self, purchase_amount):
        self.max_amount = 0
        self.total_amount = 0
        self.purchase_amount = purchase_amount
        self.avg_price = 0
        self.income = 0
        self.buy_cnt = 0

    def deal(self, curr_price):
        if self.total_amount == 0:
            self.total_amount = self.purchase_amount / curr_price
            self.avg_price = curr_price
            self.buy_cnt = 1
        elif self.avg_price < curr_price:
            self.income = self.income + (self.total_amount*curr_price - self.total_amount*self.avg_price)
            self.total_amount = 0
        else:
            curr_amount = (self.purchase_amount / curr_price) / self.buy_cnt
            total_price = (self.total_amount*self.avg_price) + (curr_amount*curr_price)
            if total_price > self.max_amount:
                self.max_amount = total_price
            self.total_amount = self.total_amount + curr_amount
            self.avg_price = total_price / self.total_amount
            self.buy_cnt = self.buy_cnt + 1
