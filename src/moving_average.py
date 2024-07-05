import pandas as pd

class MovingAverage:
    def __init__(self, df):
        self.df = df

    def calculate(self, window=3):
        return self.df.select_dtypes(include=[float, int]).rolling(window=window).mean()
