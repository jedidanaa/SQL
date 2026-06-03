"""
You are building a Football Player Management System. Create a players table 
with details like name, club, nationality, age, and city. Insert at least 6 
famous football players. Then using a subquery, find all players who play 
for the same club as 'Messi'.
"""
import sqlite3

conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        club TEXT NOT NULL,
        nationality TEXT NOT NULL,
        age INTEGER NOT NULL,
        city TEXT NOT NULL
    )
""")

# Insert famous football players
cursor.executemany("""
    INSERT INTO players (name, club, nationality, age, city) VALUES (?, ?, ?, ?, ?)
""", [
    ("Lionel Messi",       "Inter Miami",  "Argentina", 36, "Miami"),
    ("Cristiano Ronaldo",  "Al Nassr",     "Portugal",  39, "Riyadh"),
    ("Sergio Busquets",    "Inter Miami",  "Spain",     35, "Miami"),
    ("Jordi Alba",         "Inter Miami",  "Spain",     34, "Miami"),
    ("Kylian Mbappe",      "Real Madrid",  "France",    25, "Madrid"),
    ("Vinicius Jr",        "Real Madrid",  "Brazil",    23, "Madrid"),
    ("Erling Haaland",     "Man City",     "Norway",    23, "Manchester"),
])

conn.commit()
print("Players inserted successfully!\n")

# Fetch all players
cursor.execute("SELECT * FROM players")
rows = cursor.fetchall()
print(" All Players:")
print(f"{'ID':<5} {'Name':<20} {'Club':<15} {'Nationality':<15} {'Age':<5} {'City':<12}")
print("-" * 75)
for row in rows:
    print(f"{row[0]:<5} {row[1]:<20} {row[2]:<15} {row[3]:<15} {row[4]:<5} {row[5]:<12}")

# Subquery — find all players from the same club as Messi
print("\n🔍 Subquery: Players from the same club as 'Messi':")
cursor.execute("""
    SELECT * FROM players
    WHERE club = (
        SELECT club FROM players WHERE name = 'Lionel Messi'
    )
    AND name != 'Lionel Messi'
""")
subquery_rows = cursor.fetchall()
print(f"{'ID':<5} {'Name':<20} {'Club':<15} {'Nationality':<15} {'Age':<5} {'City':<12}")
print("-" * 75)
for row in subquery_rows:
    print(f"{row[0]:<5} {row[1]:<20} {row[2]:<15} {row[3]:<15} {row[4]:<5} {row[5]:<12}")

conn.close()