import pandas as pd
import os


def indexing(file_name):
    file = os.path.join('Data', file_name)
    table = pd.read_csv(file, index_col=0)
    pd.set_option('display.max_columns', None)
    #print(table.head())
    print(table.country)
    print(table['country'])  # table['country'] == table.country
    print(table['country'][0])
    print(table.iloc[0])


def index_based_selection(file_name):
    file = os.path.join('Data', file_name)
    table = pd.read_csv(file, index_col=0)
    pd.set_option('display.max_columns', None)
    print()

if __name__ == '__main__':
    indexing('winemag-data-130k-v2.csv')
