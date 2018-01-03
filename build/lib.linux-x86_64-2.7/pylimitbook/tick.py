#!/usr/bin/python

class Tick(object):
    def __init__(self, data):
        self.timestamp = int(data['quote_tm'])
        self.qty = int(data['vol_orgnl'])
        self.price = convert_price(data['limit_prc'], True)
        self.id_num = data['order_no']
        

def convert_price(price, use_float):
    if use_float:
        return float(price)

class Trade(Tick):
    def __init__(self, data):
        super(Trade, self).__init__(data)

class Ask(Tick):
    def __init__(self, data):
        super(Ask, self).__init__(data)
        self.is_bid = False
        self.activity_typ = data['activity_typ']

class Bid(Tick):
    def __init__(self, data):
        super(Bid, self).__init__(data)
        self.is_bid = True
        self.activity_typ = data['activity_typ']
