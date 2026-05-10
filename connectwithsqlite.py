"""
# Import file from your system 
from google.colab inport files
file = files.upload()
"""
import sqlite3
database = 'database.sqlite'
conn = sqlite3.connect(database)
print("Opened data successfully")
import pandas as pd
tables = pd.read_sql("""   SELECT * 
                    from sqlite_master
                    Where type='table';""", conn)
print(tables)