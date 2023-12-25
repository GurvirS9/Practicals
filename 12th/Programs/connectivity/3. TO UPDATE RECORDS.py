import mysql.connector as sqltor
mycon = sqltor.connect(host='localhost', user = 'root', passwd = 'root')
cursor = mycon.cursor()
cursor.execute('use db2')

no = eval(input('Enter RNo of student to update: '))
cursor.execute('select * from student where rno={}'.format(no))
for rec in cursor:
    print(rec)
cursor.execute('describe student')
for colname in cursor:
    print(colname[0])
field = input('Enter field you want to update: ')
val = input('Enter the new value: ')
cursor.execute("update student set {}='{}' where rno={}".format(field, val, no))
mycon.commit()
print('Record updated successfully')

