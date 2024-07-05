import os
import sys

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to Python's sys.path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

import pandas as pd

from src.dataframe_statistical_analyzer import DataFrameAnalyzer

if __name__ == "__main__":
    data = {
        "month": [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
        "stock_price": [
            50.0,
            51.5,
            49.8,
            52.0,
            53.2,
            54.0,
            55.0,
            56.0,
            57.5,
            59.0,
            60.0,
            61.0,
        ],
    }

    df = pd.DataFrame(data)
    a = DataFrameAnalyzer(df)
    print(a.analyze())
