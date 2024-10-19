from rqalpha.api import *
from rqalpha import run_func
import rqalpha as rq

import numpy as np
import pandas as pd

# 初始化策略
def init(context):
    index = '000300.XSHG'  # 选择沪深300作为股票池
    context.stock_pool = index_components(index) 

    # 设置回测的窗口期
    context.rebalance_period = 30  # 换仓间隔，可以调整
    
    context.factor_name = 'market_cap'  # 使用市值作为因子
    context.days_count = -1  # 跟踪天数，便于执行定期调仓

# 处理bar数据的函数
def handle_bar(context, bar_dict):
    context.days_count += 1

    # 每隔context.rebalance_period天执行一次调仓
    if context.days_count % context.rebalance_period == 0:
        # 获取股票池中所有股票在过去一个调仓周期内的市值数据
        factors = get_factor(context.stock_pool, 'market_cap', count=1, expect_df=False)

        # 把因子从高到低进行排序
        market_caps_sorted = factors.sort_values(ascending=False)

        #quantiles = market_caps_sorted.quantile([i/10 for i in range(1, 11)])
        #long_group = market_caps_sorted[market_caps_sorted > quantiles[0.9]]
        #short_group = market_caps_sorted[market_caps_sorted <= quantiles[0.1]]
        #long_group_list = long_group.index.tolist()
        #short_group_list = short_group.index.tolist()

        # 选择排名最前的10只股票，即市值最高的10只
        long_group = market_caps_sorted[-10:]
        long_group_list = long_group.index.tolist()
        short_group = market_caps_sorted[:10]
        short_group_list = short_group.index.tolist()

        print("做多组:", long_group_list)
        print("做空组:", short_group_list)

        # 获取当前投资组合中的股票列表
        current_positions = list(context.portfolio.positions.keys())
        print("当前持仓股票:", current_positions)

        # 如果第一次直接pass
        if not current_positions:
            pass
        # 如果有股票持仓，先平仓
        else:
            for stock in current_positions:
                # 不在榜单直接清空
                if stock not in long_group_list and stock not in short_group_list:
                    print("清仓：", stock)
                    order_target_percent(stock, 0)

        # 再用剩下的钱分配榜单中的股票
        # 定义做多和做空的每只股票对应的权重
        long_weight_per_stock = 1 / len(long_group_list)
        print("做多权重：", long_weight_per_stock)
        short_weight_per_stock = -0.5 / len(short_group_list)
        print("做空权重：", short_weight_per_stock)

        # 对做多名单中的股票调整仓位
        for stock in long_group_list:
            # 注意这个是以当前可用
            order_percent(stock, long_weight_per_stock)
        
        # 对做空名单中的股票调整仓位
        #for stock in short_group_list:
        #    order_percent(stock, short_weight_per_stock)