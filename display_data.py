"""
This module is used in order to display the data
in a complete and good-looking way
"""

import pandas as pd
from tabulate import tabulate


def display_table(data):
    """
    Get the weather information and display it in a nice way through a table
    :param data: weather information
    :return: table to be displayed to the user in which there are the
    weather, the temperature, the description, the icon of the requested city
    or its history
    """
    # create a list of dictionaries
    data = [data] if type(data) is dict else data
    # create a dataframe
    df = pd.DataFrame(data)
    if 'id' in df.columns:
        df.drop(['id'], axis=1, inplace=True)
    # use capital letters for the headers
    df.columns = df.columns.str.upper()
    # create the table using tabulate
    table = tabulate(df, headers='keys', showindex=False)
    print(table)
