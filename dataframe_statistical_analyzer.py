import pandas as pd
from src.summary_statistics import SummaryStatistics
from src.pct_change import PercentageChange
from src.outliers_iqr import OutliersIQR
from src.dips import Dips
from src.trend_analysis import TrendAnalysis
from src.moving_average import MovingAverage
from src.correlation_analysis import CorrelationAnalysis
from src.increases import Increases


class DataFrameAnalyzer:
    def __init__(self, df):
        self.df = df
        self.summary_stats = SummaryStatistics(df)
        self.pct_change = PercentageChange(df)
        self.outliers_iqr = OutliersIQR(df)
        self.dips = Dips(df)
        self.trend_analysis = TrendAnalysis(df)
        self.moving_average = MovingAverage(df)
        self.correlation_analysis = CorrelationAnalysis(df)
        self.increases = Increases(df)

    def analyze(self):
        output = []
        output.append("\nSummary Statistics:")
        output.append(str(self.summary_stats.calculate()))

        output.append("\nMonth-to-Month Percentage Changes:")
        output.append(str(self.pct_change.calculate()))

        output.append("\nOutliers Detection IQR:")
        output.append(str(self.outliers_iqr.detect()))

        output.append("\nCalculating Dips:")
        output.append(str(self.dips.calculate()))

        output.append("\nTrend Analysis (Linear Regression):")
        for column, (slope, intercept) in self.trend_analysis.analyze().items():
            output.append(f"Column: {column}, Slope: {slope}, Intercept: {intercept}")

        output.append("\nMoving Average (3 months window):")
        output.append(str(self.moving_average.calculate()))

        output.append("\nCalculating Increases:")
        output.append(str(self.increases.calculate()))

        output.append("\nCorrelation Analysis:")
        output.append(str(self.correlation_analysis.calculate()))

        output.append("\nFinal DataFrame:")
        output.append(str(self.df))

        return "\n".join(output)
