import sqlite3

conn = sqlite3.connect('database.sqlite')

print("Opened database successfully")

conn.execute('''CREATE TABLE CLASS_10
        (SNO INT PRIMARY KEY NOT NULL,
        Roll_No INT NOT NULL,
        Name TEXT NOT NULL,
        AGE INT DEFAULT (15),
        GENDER TEXT NOT NULL,
        Email_ID TEXT NOT NULL,
        Contact_No REAL NOT NULL); ''')

print("Table created successfully")
conn.execute("INSERT INTO CLASS_10(SNO,Roll_No,Name,AGE,Gender,Email_ID, Contact_No) \
     VALUES(1,1, 'Allen',14, 'Male', 'allen@gmail.com',0712345)");

conn.execute("INSERT INTO CLASS_10(SNO,Roll_No,Name,AGE,Gender,Email_ID, Contact_No) \
     VALUES(2, 2, 'Jedida',14, 'Female', 'Jedida@gmail.com',0712142)");

conn.execute("INSERT INTO CLASS_10(SNO,Roll_No,Name,AGE,Gender,Email_ID, Contact_No) \
     VALUES(3, 3, 'Laurel',14, 'Female', 'Laurel@gmail.com',0212349)");
     
conn.commit()
print("Records created successfully")
import pandas as pd
tables = pd.read_sql("""SELECT *
                    FROM sqlite_master
                    WHERE type= 'table';""",conn)

print(tables)
class_10d = pd.read_sql("""SELECT *
                        FROM CLASS_10;""",conn)
print(class_10d.head())