import pandas as pd


class SummaryStatistics:
    def __init__(self, df):
        self.df = df

    def calculate(self):
        return self.df.describe(include="all")
