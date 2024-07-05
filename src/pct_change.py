import pandas as pd

class PercentageChange:
    def __init__(self, df):
        self.df = df

    def calculate(self, periods=1):
        return (self.df.select_dtypes(include=[float, int]).pct_change(periods=periods) * 100).round(2)
