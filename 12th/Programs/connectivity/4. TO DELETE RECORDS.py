import mysql.connector as sqltor
mycon = sqltor.connect(host='localhost', user = 'root', passwd = 'root')
cursor = mycon.cursor()
cursor.execute('use db2')

no = eval(input('Enter RNo. of student you want to remove: '))
cursor.execute("select * from student where rno={}".format(no))
for rec in cursor:
    print(rec)
ch = input('Are you sure you want to remove this student? (y/n): ')
if ch == 'y':
    cursor.execute('delete from student where rno={}'.format(no))
    mycon.commit()
    print('Record removed successfully')

