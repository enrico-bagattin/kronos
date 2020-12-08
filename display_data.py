"""
This module is used in order to display the data in a complete and good-looking way
"""

import pandas as pd
from tabulate import tabulate

def display_table(data):
    """
    Get the weather information and display it in a nice way through a table
    :param data: weather information
    :return: table to be displayed to the user in which there are the weather, the temperature, the description and
    the icon of the requested city or its history 
    """
    data = [data] if type(data) is dict else data  #create a list of dictionaries
    df = pd.DataFrame(data) #create a dataframe
    if 'id' in df.columns:
        df.drop(['id'], axis=1, inplace=True) #drop the id column if it exists
    df.columns = df.columns.str.upper() #use capital letters for the headers
    table = tabulate(df, headers='keys', showindex=False) #create the table using tabulate
    print(table)
