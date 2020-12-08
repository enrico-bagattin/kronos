"""
This module is used to retrieve data on air quality
from the air_quality dataset
"""
import pandas as pd
import math

pd.options.mode.chained_assignment = None  # default='warn'


def get_air_quality(city):
    """
    Get air quality information
    :param: city
    :return: quality air annual mean
    """
    df = pd.read_csv('datasets/air_quality.csv')
    df1 = df[['City', 'Annual.mean']]
    df2 = df1[pd.to_numeric(df1['Annual.mean'], errors='coerce').notnull()]
    df2["Annual.mean"] = pd.to_numeric(df2["Annual.mean"])

    air_level = df2.loc[df2.City == city, 'Annual.mean'].mean()

    if math.isnan(air_level):
        return 'n.d.'
    icon = u"\U0001F7E2"  # Green circle
    if air_level > 50:
        icon = u"\U0001F7E0"  # Orange circle
    if air_level > 150:
        icon = u"\U0001F534"  # Red circle
    if air_level > 300:
        icon = u"\U0001F7E3"  # Purple circle

    return icon + ' ' + str(air_level)
