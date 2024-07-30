import sqlite3

# making a connection to sqllite
connection = sqlite3.connect("employee.db")

# the cursor object will help in creating table, inserting record etc.
cursor = connection.cursor()

cursor.execute('''DROP TABLE EMPLOYEE;''')



connection.commit()
connection.close()