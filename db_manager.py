"""
Manage database to store wether history informations
"""
from sqlite3 import connect
from datetime import datetime

DB_PATH = 'datasets/history.db'
conn = None
cursor = None

def dict_factory(db_cursor, row):
"""
    Converts retriven data in a dictionary
    """
    d = {}
    for idx, col in enumerate(db_cursor.description):
        d[col[0]] = row[idx]
    return d


def open_and_create(verbosity=0):
"""
    This function check for the existence of wether forecast 
    table and if it does not exist, it creates one.
    """
    global conn
    global cursor
    conn = connect(DB_PATH)
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute("SELECT count(name) as table_exists FROM sqlite_master WHERE type='table' AND name='weather_forecasts'")
    if cursor.fetchone()['table_exists'] == 0:
        create_weather_forecasts_table()


def create_weather_forecasts_table():
"""
    This fuctions is used to create the table in the DB
    """
    global conn
    global cursor
    cursor.execute('''CREATE TABLE weather_forecasts
                   (id INTEGER,
                    timestamp DATE NOT NULL,
                    city VARCHAR(255) NOT NULL,
                    forecast VARCHAR(255) NOT NULL,
                    temperature VARCHAR(6),
                    icon VARCHAR(15),
                    PRIMARY KEY (id))''')
