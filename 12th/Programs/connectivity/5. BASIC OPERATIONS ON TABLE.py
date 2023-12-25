import mysql.connector as sqltor
mycon = sqltor.connect(host='localhost', user = 'root', passwd = 'root')
cursor = mycon.cursor()
cursor.execute('use db2')

def checkconnect():
    if mycon.is_connected():
        print('MySQL is connected')
    else:
        print('MySQL is not connected')

def viewrec():
    cursor.execute('select * from student')
    data = cursor.fetchall()
    count = cursor.rowcount
    for row in data:
        print(row)
    print(count, 'rows in table')

def insertrec():
    ch = 'y'
    while ch == 'y':
        print('Enter student details below:')
        no = eval(input('Roll No.: '))
        name = input('Name: ')
        std = input('Grade: ')
        cursor.execute("insert into student value({},'{}',{})".format(no, name, std))
        mycon.commit()
        print('Record added successfully')
        ch = input('Want to enter more? (y/n): ')

def updaterec():
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

def deleterec():
    no = eval(input('Enter RNo. of student you want to remove: '))
    cursor.execute("select * from student where rno={}".format(no))
    for rec in cursor:
        print(rec)
    ch = input('Are you sure you want to remove this student? (y/n): ')
    if ch == 'y':
        cursor.execute('delete from student where rno={}'.format(no))
        mycon.commit()
        print('Record removed successfully')

#MENU
mc='y'
while mc=='y':
    print('===================================')
    print('MySQL Operations')
    print('===================================')
    print('1. Check Connection with MySQL')
    print('2. View records')
    print('3. Insert records')
    print('4. Update records')
    print('5. Delete records')
    print('===================================')
    ch = int(input('Enter choice (1-5): '))
    if ch == 1:
        checkconnect()
    elif ch == 2:
        viewrec()
    elif ch == 3:
        insertrec()
    elif ch == 4:
        updaterec()
    elif ch == 5:
        deleterec()
    else:
        print('Invalid choice')
    mc=input('Want to perform more operations? (y/n): ')
else:
    print('See you soon!')

