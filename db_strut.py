import sqlite3

# Database setup for sqlite3 to store customer data
# from different uses of the program
connection = sqlite3.connect('customerTable.db')
crsr = connection.cursor()
sql_command = """CREATE TABLE emp (
cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
cust_name VARCHAR(30),
phone_num VARCHAR(20),
purchase VARCHAR(100),
del_date DATE);"""

#crsr.execute(sql_command)