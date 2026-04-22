import sqlite3

conn = sqlite3.connect("users.db")

conn.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    email TEXT,
    password TEXT
)
""")

print("Database created successfully!")
conn.close()