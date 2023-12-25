import pickle as p

def create():
    myfile = open("teacher1.dat", "wb+")
    ch = 'y'
    while ch == 'y':
        age = eval(input("Enter age: "))
        name = input("Enter name: ")
        exp = eval(input("Enter experience: "))
        strec = {"Age":age, "Name":name, "Experience":exp}
        p.dump(strec, myfile)
        ch = input("Want to enter more? (y/n): ")
    print("Records added successfully")
    myfile.close()

def add():
    myfile = open("teacher1.dat", "ab+")
    ch = 'y'
    while ch == 'y':
        age = eval(input("Enter age: "))
        name = input("Enter name: ")
        exp = eval(input("Enter experience: "))
        strec = {"Age":age, "Name":name, "Experience":exp}
        p.dump(strec, myfile)
        ch = input("Want to enter more? (y/n): ")
    print("Records added successfully")
    myfile.close()

def display():
    myfile = open("teacher1.dat","rb")
    print("Teachers with experience between 5 and 10 years")
    print("{0:^10} {1:<20} {2:>8}".format("Age","Name","Experience"))
    print("==========================================")
    try: 
        while True:
            l = p.load(myfile)
            if l["Experience"]>5 and l["Experience"]<10:
                print("{0:^10} {1:<20} {2:>8}".format(l["Age"],l["Name"],l["Experience"]))
    except EOFError:
        pass
    myfile.close()

ch = 'y'
while ch == 'y':
    print("          MENU           ")
    print("1. Create file")
    print("2. Add record")
    print("3. Display records with condition")
    print("4. Exit")
    c = eval(input("Enter choice: "))
    if c == 1:
        create()
    elif c == 2:
        add()
    elif c == 3:
        display()
    elif c == 4:
        break
    else:
        print("Invalid choice")

