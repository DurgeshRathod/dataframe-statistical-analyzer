from setuptools import find_packages, setup

setup(
    name="DataFrameAnalyzer",
    version="1.0.0",
    description="A Python package for dataframe based summary statistics calculation, percentage change computation, outlier detection, trend analysis, moving average calculation, correlation analysis, and seasonal pattern interpretation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DurgeshRathod/dataframe-statistical-analyzer.git",
    author="Durgesh Rathod",
    author_email="durgeshrathod.777@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "scipy",
        "scikit-learn",
        "statsmodels",
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
