import sqlite3


def get_connection():
    con= sqlite3.connect("expenses.db")
    return con

def create_table():
    con= get_connection()
    cursor=con.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expense(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT,
    date TEXT 
    )
     ''')
    con.commit()
    con.close()

create_table()

