import pandas as pd

class Increases:
    def __init__(self, df):
        self.df = df

    def calculate(self):
        increases = {}
        for column in self.df.select_dtypes(include=[float, int]).columns:
            mean = self.df[column].mean()
            std_dev = self.df[column].std()
            threshold = mean + std_dev
            increases[column] = self.df[self.df[column] > threshold]
        return increases
