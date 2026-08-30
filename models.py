import sqlite3
from database import get_connection

def add_expense(title,amount,category,date):
    con =get_connection()
    cursor=con.cursor() 
    cursor.execute('''
INSERT INTO EXPENSE(title,amount,category,date)
VALUES(?,?,?,?) 
''',(title,amount,category,date))
    con.commit()
    con.close()
    return"ADDED"

print(add_expense("Groceries",50.0,"Food","2024-06-01"))    