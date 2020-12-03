


import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'

def get_air_quality (city):
    df = pd.read_csv('WHO_air_quality_database_2018_v14_merged.csv')
    df1 = df[['City', 'Annual.mean']]
    df2=df1[pd.to_numeric(df1['Annual.mean'], errors='coerce').notnull()]
    df2["Annual.mean"] = pd.to_numeric(df2["Annual.mean"])

    return df2.loc[df2.City == city, 'Annual.mean'].mean()
