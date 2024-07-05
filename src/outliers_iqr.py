import pandas as pd

class OutliersIQR:
    def __init__(self, df):
        self.df = df

    def detect(self):
        outliers = {}
        for column in self.df.select_dtypes(include=[float, int]).columns:
            q1 = self.df[column].quantile(0.25)
            q3 = self.df[column].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            outliers[column] = self.df[(self.df[column] < lower_bound) | (self.df[column] > upper_bound)]
        return outliers
