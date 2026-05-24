
import numpy as np
import pandas as pd
import sqlite3

database = 'database.sqlite' 

conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT *
                        FROM sqlite_master
                        WHERE type= 'table'""",conn)

print(tables)

joined_city = pd.read_sql("""SELECT c.Country_Id, c.Country_name, ci.City_Name
                             FROM Country c
                             INNER JOIN city ci
                             ON c.Country_Id == ci.Country_id""",conn)

print(joined_city)

joined_left = pd.read_sql("""SELECT * 
                             FROM player
                             LEFT JOIN season
                             ON player,Player__Id == season.Man_Of_The_Series""", conn)

print(joined_left)

joined_cross = pd.read_sql("""SELECT c.c.Country_Id, c.Country_name, ci.City_Name
                             FROM Country c
                             CROSS JOIN city ci""",conn)

print(joined_cross)

union = pd.read_sql("""SELECT Player_Name
                       FROM Player
                       UNION
                       SELECt Team_Name
                       FROM team""" , conn)

print(union)
