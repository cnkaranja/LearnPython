# verify_sqlite.py
import sqlite3

print("SQLite library version:", sqlite3.sqlite_version)
with sqlite3.connect("test.db") as conn:
    rows = conn.execute("SELECT id, msg FROM greetings").fetchall()
    print(rows)  # [(1, 'hello'), (2, 'hola')]
