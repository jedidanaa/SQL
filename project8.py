import sqlite3

def run_queries(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Example 1: Select all rows
    cursor.execute("SELECT * FROM employees;")
    print("All employees:", cursor.fetchall())

    # Example 2: Filter with WHERE clause
    cursor.execute("SELECT name, department FROM employees WHERE department='Sales';")
    print("Sales employees:", cursor.fetchall())

    # Example 3: Find minimum salary
    cursor.execute("SELECT MIN(salary) FROM employees;")
    print("Lowest salary:", cursor.fetchone()[0])

    # Example 4: Find maximum salary
    cursor.execute("SELECT MAX(salary) FROM employees;")
    print("Highest salary:", cursor.fetchone()[0])

    # Example 5: Min/Max with WHERE
    cursor.execute("""
        SELECT MIN(salary), MAX(salary) 
        FROM employees 
        WHERE department='Sales';
    """)
    print("Sales salary range:", cursor.fetchone())

    conn.close()

# Replace with your actual database file
run_queries("your_database.db")

