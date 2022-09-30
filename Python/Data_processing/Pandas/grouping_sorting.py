import pandas as pd
import os


def read_csv(file_name):
    file = os.path.join('Data', file_name)
    table = pd.read_csv(file, index_col=0)
    return table


def pd_groupby(df):
    pd.set_option('display.max_columns', None)
    new_df = df.groupby('points').points.count()  # this is equal df.points.value_count()
    new_df2 = df.groupby('points').price.min()  # find the cheapest wine in each point category
    new_df3 = df.groupby('winery').apply(lambda df: df.title.iloc[0])  # print first wine title for each winery
    # new_df4 -- find the best wine in country and province
    new_df4 = df.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
    new_df5 = df.groupby(['country', 'province']).apply(lambda df: df.points.loc[df.points.idxmax()])  # points only
    new_df6 = df.groupby('country').price.agg([len, min, max])  # количество в стране, мин и макс цена в стране
    # print(new_df6)


def pd_sorting(df):
    pd.set_option('display.max_columns', None)
    new_df = df.sort_values(by=['price'], ascending=False)
    new_df2 = new_df.loc[:, ['title', 'country', 'price']]  # sorted by price table: id | title | country | price
    print(new_df2)


def reviews_written(df):
    """Who are the most common wine reviewers in the dataset? Create a Series whose index is the taster_twitter_handle
    category from the dataset, and whose values count how many reviews each person wrote."""
    new_df = df.groupby('taster_twitter_handle').apply(len)
    return df


def best_rating_per_price(df):
    """What is the best wine I can buy for a given amount of money? Create a Series whose index is wine prices and
    whose values is the maximum number of points a wine costing that much was given in a review. Sort the values
    by price, ascending (so that 4.0 dollars is at the top and 3300.0 dollars is at the bottom)."""
    new_df = df.groupby('price').apply(lambda df: df.loc[df.points.idxmax()])
    new_df = new_df.loc[:, ['points']].squeeze()
    print(new_df, type(new_df))
    # shorter:
    best_rating_per_price = df.groupby('price')['points'].max().sort_index()
    return best_rating_per_price


def price_extremes(df):
    """What are the minimum and maximum prices for each variety of wine? Create a DataFrame whose index
    is the variety category from the dataset and whose values are the min and max values thereof."""
    return df.groupby('variety').price.agg([min,max])

def most_expensive_wine_varieties(df):
    """What are the most expensive wine varieties? Create a variable sorted_varieties containing a copy of the
    dataframe from the previous question where varieties are sorted in descending order based on minimum price,
    then on maximum price (to break ties)."""
    df = df.groupby('variety').price.agg([min,max])
    return df.sort_values(by=['min','max'], ascending=False)


def reviewer_mean_ratings(df):
    """Create a Series whose index is reviewers and whose values is the average review score given out by that reviewer.
    Hint: you will need the taster_name and points columns."""
    return df.groupby('taster_name')['points'].mean()

def country_variety_counts(df):
    """What combination of countries and varieties are most common? Create a Series whose index
    is a MultiIndexof {country, variety} pairs. For example, a pinot noir produced in the US
    should map to {"US", "Pinot Noir"}. Sort the values in the Series in descending order based on wine count."""
    return df.groupby(['country', 'variety']).size().sort_values(ascending=False)


if __name__ == '__main__':
    df = read_csv(file_name='winemag-data-130k-v2.csv')
    # pd_groupby(df)
    pd_sorting(df)
