import pandas as pd

class CorrelationAnalysis:
    def __init__(self, df):
        self.df = df

    def calculate(self):
        return self.df.select_dtypes(include=[float, int]).corr()
