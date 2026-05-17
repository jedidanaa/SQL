#import dataset 
# connect with sqlite database 
#import necessary libraries 
import sqlite3 
database = 'database.sqlite'
conn = sqlite3.connect(database)
print('Opened data sucessfully')

#Read SQL query for getting all the tables of database into a database 
import pandas as pd 
tables = pd.read_sql("""SELECT *
                         FROM sqlite_master
                         WHERE type= 'table';""",conn)

print(tables)
matches = pd.read_sql("""SELECT *
                         FROM Match;""",conn)

print(matches.head())

result1 = pd.read_sql("""SELECT AVG(win_Margin),Match_Winner 
                           FROM Match
                           WHERE Season_id == 9
                           Group by Match_Winner
                           ORDER BY AVG(win_Margin);""",conn )

print(result1)
result2 = pd.read_sql("""SELECT COUNT(DISTINCT Venue_id)
                         FROM Match
                         WHERE Season_id == 9;""",conn)

print(result2)
result3 = pd.read_sql("""SELECT Min(Win_Margin), Max(Win_Margin), Avg(Win_Margin), COUNT(DISTINCT(Man_Of_The_Match))
                         FROM Match;""",conn)

print(result3)