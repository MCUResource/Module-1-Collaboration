import sqlite3
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS books (
                   title TEXT,
                   author TEXT,
                   year INTEGER
                   )
               """)
conn.commit()
conn.close()
print("Database and table created successfully")
