import os
import pandas as pd

"""
1. Creating data
There are two core objects in pandas: the DataFrame and the Series.
DataFrame is a table
Series is a list
"""


def first_dataframe():
    table1 = pd.DataFrame({'Yes': [51, 21], 'No': [131, 2]})
    print(table1)

    table2 = pd.DataFrame({'Bob': ['I liked it', 'It was awful'],
                           'Sue': ['Pretty good', 'Bland']},
                          index=['Product A', 'Product B'])
    print(table2)


def first_series():
    """Series doesn't have a column name, it only has one overall name
    DataFrame is a bunch of Series glued together"""
    series1 = pd.Series([1, 2, 3, 4, 5])
    print(series1)

    series2 = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='ProductA')
    print(series2)


"""
2. Reading Data
"""


def save_data_files(file_name):
    animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
    file = os.path.join('Data', file_name)
    animals.to_csv(file)


def read_data_files(file_name):
    file = os.path.join('Data', file_name)
    wine_reviews = pd.read_csv(file, index_col=0)  # set number of column with index
    print(wine_reviews.shape)  # size of the DataFrame
    # pd.set_option('display.max_columns', 2)
    print(wine_reviews.head())  # first 5 rows


if __name__ == '__main__':
    first_dataframe()
    first_series()
    save_data_files('cows_and_goats.csv')
    read_data_files('cows_and_goats.csv')
