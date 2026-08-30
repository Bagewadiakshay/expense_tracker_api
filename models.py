import sqlite3
from database import get_connection

#add funn
def add_expense(title,amount,category,date):
    con =get_connection()
    cursor=con.cursor() 
    cursor.execute('''
INSERT INTO expense(title,amount,category,date)
VALUES(?,?,?,?) 
''',(title,amount,category,date))
    con.commit()
    con.close()
    return"ADDED"

#display all funn
def get_allexp():
    con = get_connection()
    cursor = con.cursor()
    cursor.execute('''   
select * from expense
''')#expensces db
    rows = cursor.fetchall()
    con.close()
    return rows

#new function of delete and upodate
def del_exp(expense_id):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute(
        "DELETE FROM expense  WHERE id=?" ,(expense_id,)
    )
    con.commit()
    con.close()
    return "deleted..."

def upd_exp(expense_id,amount):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute(
        "UPDATE expense SET amount=? WHERE id=?",(amount,expense_id)
        )
    con.commit()
    con.close()
    return"uploaded "

#testing 

# print(add_expense("Groceries", 50.0, "Food", "2024-06-01"))
# print(add_expense("Lunch", 250, "Food", "2026-08-30"))
# print(add_expense("Bus", 50, "Travel", "2026-08-30"))

    # print(get_allexp())
    # print(del_exp(1))
    # print(upd_exp(2, 999.0))
    # print(get_allexp())

