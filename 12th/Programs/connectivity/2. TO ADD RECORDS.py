import mysql.connector as sqltor
mycon = sqltor.connect(host='localhost', user = 'root', passwd = 'root')
cursor = mycon.cursor()
cursor.execute('use db2')

ch = 'y'
while ch == 'y':
    print('Enter student details below:')
    no = eval(input('Roll No.: '))
    name = input('Name: ')
    std = input('Std: ')
    cursor.execute("insert into student value({},'{}',{})".format(no, name, std))
    mycon.commit()
    print('Record added successfully')
    ch = input('Want to enter more? (y/n): ')

