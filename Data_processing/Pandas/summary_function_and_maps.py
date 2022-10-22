import pandas as pd
import os


def read_csv(file_name):
    file = os.path.join('Data', file_name)
    df = pd.read_csv(file, index_col=0)
    return df


def summary_functions(df):
    print(df.points.describe())  # count, mean, std, min, 25%, 50%, 75%, max (for numerical data)
    print(df.country.describe())  # count, unique, top, freq (for string data)
    print(df.country.unique())  # print list of unique values
    print(df.country.value_counts())  # how often they occur in data set


def first_map(df):
    points_mean = df.points.mean()
    new_df = df.points.map(lambda p: p - points_mean)  # using map to create list of deviation from mean
    print(new_df)
    new_df2 = df.points-points_mean  # faster, than map
    print(new_df2)
    new_df3 = df.country + '-' + df.region_1
    print(new_df3)

def find_title_wine_by_ratio(df):
    """I'm an economical wine buyer. Which wine is the "best bargain"? Create a variable bargain_wine with the title of
    the wine with the highest points-to-price ratio in the dataset."""
    best_ratio_id = (df.points / df.price).idxmax()
    bargain_wine = df.title.iloc[best_ratio_id]
    print(bargain_wine)


def sum_words_in_data_frame_column(df):
    """There are only so many words you can use when describing a bottle of wine.
    Is a wine more likely to be "tropical" or "fruity"?
    Create a Series descriptor_counts counting how many times each of these two words appears in the description column
    in the dataset. (For simplicity, let's ignore the capitalized versions of these words.)"""
    check_tropical = df['description'].str.contains('tropical').sum()
    check_fruity = df['description'].str.contains('fruity').sum()
    descriptor_counts = pd.Series([check_tropical, check_fruity], index=['tropical', 'fruity'])
    print(descriptor_counts)


def convert_rating_system(df):
    """We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points
    is too hard to understand - we'd like to translate them into simple star ratings. A score of 95 or higher
    counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.
    Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should
    automatically get 3 stars, regardless of points. Create a series star_ratings with the number of stars
    corresponding to each review in the dataset."""

    def n_stars(row):
        if row.country == 'Canada':
            return 3
        elif row.points >= 95:
            return 3
        elif row.points >= 85:
            return 2
        else:
            return 1

    new_df = df.apply(n_stars, axis='columns')
    print(new_df)


if __name__ == '__main__':
    df = read_csv('winemag-data-130k-v2.csv')
    summary_functions(df)
    first_map(df)
    convert_rating_system(df)