import pandas as pd
import os


def read_csv(file_name):
    file = os.path.join('Data', file_name)
    df = pd.read_csv(file, index_col=0)
    return df


def renaming(df):
    pd.set_option('display.max_columns', None)
    new_df = df.rename(columns={'points': 'score'})  # rename points column
    new_df = df.rename(index={0: 'firstEntry', 1: 'secondEntry'})  # rename some elements of the index
    new_df = df.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')  # rename rows & cols


def combining():
    df1 = pd.DataFrame({'A': ['5', '87', '42', '43'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})

    df2 = pd.DataFrame({'A1': ['43', '3', '80', '5'],
                        'B1': ['B4', 'B5', 'B6', 'B7'],
                        'C1': ['C4', 'C5', 'C6', 'C7'],
                        'D1': ['D4', 'D5', 'D6', 'D7']})

    df_join =df1.join(df2, on=None, how='left', lsuffix='', rsuffix='', sort=False)
    df_concat = pd.concat([df1, df2])




if __name__ == '__main__':
    df = read_csv('winemag-data-130k-v2.csv')
    renaming(df)
    combining()
