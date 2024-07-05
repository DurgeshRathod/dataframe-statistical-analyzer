import pandas as pd

class Dips:
    def __init__(self, df):
        self.df = df

    def calculate(self):
        dips = {}
        for column in self.df.select_dtypes(include=[float, int]).columns:
            mean = self.df[column].mean()
            std_dev = self.df[column].std()
            threshold = mean - std_dev
            dips[column] = self.df[self.df[column] < threshold]
        return dips
