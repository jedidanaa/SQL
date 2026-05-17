import sqlite3

def list_tables(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query to get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Print table names
    print("Tables in the database:")
    for table in tables:
        print(table[0])

    # Close the connection
    conn.close()

# Example usage: replace 'your_database.db' with your actual database file path
list_tables("your_database.db")
