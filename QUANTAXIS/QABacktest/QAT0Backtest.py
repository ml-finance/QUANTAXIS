# coding:utf-8

"""
日内t0的回测框架

1. 给定每日初始的股票/现金
2. 核查每日可用股票,以及是否平仓(及如果尾盘没有买回去,要在结转的时候自动买回/卖出)

"""

class QAT0Backtest():
    def __init__(self):
        pass