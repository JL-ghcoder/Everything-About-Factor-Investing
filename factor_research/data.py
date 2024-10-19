import pandas as pd
import rqdatac as rq
#from rqdatac import *
rq.init('13308132432','zyhzp0258')

# 股票数据
class StockData:
    def __init__(self, symbol, start_date, end_date, is_index=False):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date

        if is_index:
            self.stock_list = rq.index_components(symbol)
        else:
            self.stock_list = symbol

        self.stock_prices = rq.get_price(self.stock_list, start_date=self.start_date, end_date=self.end_date, frequency='1d', fields='close')

    def print_stock_prices(self):

        return self.stock_prices
    
# 因子数据
# 'market_cap'
class FactorData:
    def __init__(self, stock_list, factor_name, start_date, end_date):
        self.stock_list = stock_list
        self.factor_name = factor_name

        self.factors = rq.get_factor(stock_list, factor_name, start_date, end_date, expect_df=True)

    def print_stock_factors(self):

        return self.factors