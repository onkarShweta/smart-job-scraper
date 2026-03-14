import sqlite3

conn = sqlite3.connect("data/jobs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
company TEXT
)
""")

conn.commit()
conn.close()

print("Database created")