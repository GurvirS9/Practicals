import mysql.connector as sqltor
mycon = sqltor.connect(host='localhost', user = 'root', passwd = 'root')
cursor = mycon.cursor()
cursor.execute('use db2')

cursor.execute('select * from student')
data = cursor.fetchall()
count = cursor.rowcount
for row in data:
    print(row)
print(count, 'rows in table')

