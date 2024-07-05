# DataFrameAnalyzer

The `DataFrameAnalyzer` project provides a robust and extensible tool for analyzing and visualizing data stored in a Pandas DataFrame. The tool encapsulates various data analysis functionalities, including summary statistics, percentage change computation, outlier detection, trend analysis, moving average calculation, correlation analysis, and seasonal pattern interpretation. The project is designed following the SOLID principles and incorporates design patterns to ensure maintainability and ease of use.

## Features

- **Summary Statistics**: Generate summary statistics for the data.
- **Percentage Change Calculation**: Calculate percentage changes over specified periods.
- **Outlier Detection**: Detect outliers using both Z-score and MAD methods.
- **Trend Analysis**: Perform linear regression to analyze trends in the data.
- **Moving Average Calculation**: Calculate moving averages over a specified window.
- **Correlation Analysis**: Compute the correlation matrix of the data.
- **Seasonal Pattern Interpretation**: Interpret seasonal patterns using Holt-Winters exponential smoothing.
- **Data Visualization**: Visualize data with trends and moving averages.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DurgeshRathod/DataFrameAnalyzer.git
   cd DataFrameAnalyzer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Import the necessary modules:
   ```python
   import pandas as pd
   from DataFrameAnalyzer import DataFrameAnalyzer
   ```

2. Prepare your DataFrame:
   ```python
   data = {
       "month": ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
       "stock_price": [50.0, 51.5, 49.8, 52.0, 53.2, 54.0, 55.0, 56.0, 57.5, 59.0, 60.0, 61.0]
   }

   df = pd.DataFrame(data)
   ```

3. Initialize the `DataFrameAnalyzer` with the DataFrame:
   ```python
   analyzer = DataFrameAnalyzer(df)
   ```

4. Perform the analysis:
   ```python
   analyzer.analyze()
   ```

## Contributing

We welcome contributions to the `DataFrameAnalyzer` project. Please fork the repository and submit a pull request with your changes. Ensure your code adheres to the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

This project utilizes several open-source libraries, including Pandas, Matplotlib, Scipy, Scikit-learn, and Statsmodels. We thank the developers and maintainers of these libraries for their invaluable contributions to the open-source community.
