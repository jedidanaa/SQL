import sqlite3

conn = sqlite3.connect('database.sqlite')

print("Opened database successfully")

import pandas as pd
tables = pd.read_sql("""SELECT *
                    FROM sqlite_master
                    WHERE type= 'table';""",conn)

print(tables)

player_match = pd.read_sql("""SELECT *
                          FROM Player_Match""",conn)

print(player_match.head())

null_player_match = pd.read_sql("""SELECT *
                          FROM Player_Match
                          WHERE Team_id IS NULL""",conn)

print(null_player_match.head())

toss_dec =  pd.read_sql("""SELECT *
                          FROM Match""",conn)

print(toss_dec)