import sqlite3

# making a connection to sqllite
connection = sqlite3.connect("employee.db")

# the cursor object will help in creating table, inserting record etc.
cursor = connection.cursor()

# storing a table creation query in a variable, which I will be executing later

table_info = """
create table Employee(Name VARCHAR(25),ID INT, DEPARTMENT VARCHAR(25), SALARY INT)
"""
cursor.execute(table_info)

# inserting some values in the table

cursor.execute('''Insert Into Employee values('Rohit',1,'Artificial Intelligence',90000000)''')
cursor.execute('''Insert Into Employee values('Sudhanshu',2,'Artificial Intelligence',95000000)''')
cursor.execute('''Insert Into Employee values('Aisha',3,'Data Science',85000000)''')
cursor.execute('''Insert Into Employee values('Vikash',4,'Data Science',87000000)''')
cursor.execute('''Insert Into Employee values('Dipesh',5,'IOT',40000000)''')
cursor.execute('''Insert Into Employee values('Neha',6,'IOT',42000000)''')
cursor.execute('''Insert Into Employee values('Ravi',7,'Machine Learning',75000000)''')
cursor.execute('''Insert Into Employee values('Maya',8,'Machine Learning',77000000)''')
cursor.execute('''Insert Into Employee values('Jai',9,'Cloud Computing',68000000)''')
cursor.execute('''Insert Into Employee values('Aarti',10,'Cloud Computing',70000000)''')
cursor.execute('''Insert Into Employee values('Kiran',11,'Cyber Security',80000000)''')
cursor.execute('''Insert Into Employee values('Ravi',12,'Cyber Security',82000000)''')
cursor.execute('''Insert Into Employee values('Sonal',13,'Software Engineering',90000000)''')
cursor.execute('''Insert Into Employee values('Raj',14,'Software Engineering',92000000)''')
cursor.execute('''Insert Into Employee values('Mohan',15,'DevOps',74000000)''')
cursor.execute('''Insert Into Employee values('Anita',16,'DevOps',76000000)''')
cursor.execute('''Insert Into Employee values('Siddharth',17,'Database Administration',83000000)''')
cursor.execute('''Insert Into Employee values('Pooja',18,'Database Administration',85000000)''')
cursor.execute('''Insert Into Employee values('Shiv',19,'Product Management',91000000)''')
cursor.execute('''Insert Into Employee values('Ritu',20,'Product Management',93000000)''')


# testing

for row in (cursor.execute('''Select * from Employee''')):
    print(row)

# closing the connection 

connection.commit()
connection.close()