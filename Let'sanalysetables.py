"""### *2. connect with SQLite Database**"""
# connect with sql database
# Import necessary database
import sqlite3

database = 'database.sqlite'
 
conn = sqlite3.connect(database)
print('opened data sucessfully')

# Read SQL query for getting all the tables of database into a dataframe
import pandas as pd 
tables = pd.read_sql("""SELECT *
                    from sqlite_master
                    WHERE type= 'table'; """,conn)   
tables

# Read Table from the database into dataframe
matches = pd.read_sql("""SELECT * 
                      FROM Match;""",conn)

#Print table info 
matches.info()
