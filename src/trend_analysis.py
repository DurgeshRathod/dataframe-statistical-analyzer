import numpy as np
from sklearn.linear_model import LinearRegression

class TrendAnalysis:
    def __init__(self, df):
        self.df = df

    def analyze(self):
        trends = {}
        for column in self.df.select_dtypes(include=[float, int]).columns:
            x = np.arange(len(self.df)).reshape(-1, 1)
            y = self.df[column].values
            model = LinearRegression().fit(x, y)
            slope = model.coef_[0]
            intercept = model.intercept_
            trends[column] = (slope, intercept)
        return trends
