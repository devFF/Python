import pandas as pd
import os


def read_csv(file_name):
    file = os.path.join('Data', file_name)
    table = pd.read_csv(file, index_col=0)
    return table


def indexing(table):
    pd.set_option('display.max_columns', None)
    # print(table.head())
    print(table.country)
    print(table['country'])  # table['country'] == table.country
    print(table['country'][0])


def index_based_selection(table):
    print(table.iloc[0])  # iloc - select by index
    print(table.iloc[0, 0])  # [row, column]
    print(table.iloc[:, 0])  # two columns: index col and country col
    print(table.iloc[0:3, 0])  # first three columns (slicing)


def label_bases_selection(table):
    print(table.loc[:, 'country'])  # loc - select by label
    print(table.loc[0, 'country'])  # [row, column]
    # print(table.loc[:, 'country'])  # two columns: index col and country col
    print(table.loc[:, 'country':'designation'])  # first three columns (slicing)
    print(table.loc[:, ['country', 'price', 'title']])


def manipulating_the_index(table):
    new_table = table.set_index("title")
    print(new_table.head())
    new_table = new_table.reset_index()
    print(new_table)


def conditional_selection(table):
    print(table.country == 'Italy')  # True/False
    print(table.loc[table.country == 'Italy'])  # print if Italy True
    print(table.loc[(table.country == 'Italy') & (table.points > 90)])  # 2 conditions with symbol &(and)
    print(table.loc[(table.country == 'Italy') & (table.points > 90)])  # 2 conditions with symbol |(or)
    print(table.loc[table.country.isin(['Italy', 'France'])])  # print if country is Italy or France
    print(table.loc[table.price.notnull()])  # print if not empty (NaN)


def assigning_data(table):
    table['country'] = 'Russia'
    print(table)


if __name__ == '__main__':
    table = read_csv('winemag-data-130k-v2.csv')
    # indexing(table)
    # index_based_selection(table)
    # label_bases_selection(table)
    # manipulating_the_index(table)
    # conditional_selection(table)
    assigning_data(table)
