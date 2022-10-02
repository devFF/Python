import pandas as pd
import os


def read_csv(file_name):
    file = os.path.join('Data', file_name)
    table = pd.read_csv(file, index_col=0)
    return table


def data_types(df):
    print(df.dtypes)  # type of data in every column
    print(df.price.dtype)  # type of the price data
    df = df.points.astype('float64')  # convert data type from int64 to float64


def missing_values(df):
    new_df = df[pd.isnull(df.country)]  # get all countries with country = NaN
    replaced_new_df = new_df.country.fillna('Unknown')  # replace NaN on Unknown
    new_df1 = df.taster_twitter_handle.replace("@kerinokeefe", "@kerino")  # replace non-null value


def task_1(df):
    """What are the most common wine-producing regions? Create a Series counting the number of times each value occurs
    in the region_1 field. This field is often missing data, so replace missing values with Unknown.
    Sort in descending order."""
    new_df = df.region_1.fillna('Unknown').value_counts()
    print(new_df)




if __name__ == '__main__':
    df = read_csv('winemag-data-130k-v2.csv')
    #data_types(df)
    #missing_values(df)
    task_1(df)