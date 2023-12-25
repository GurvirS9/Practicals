import pickle as p

def dump():
    f = open("student1.dat", "wb")
    ch = "y"
    while ch == "y":
        rno = eval(input("Enter Roll No.: "))
        name = input("Enter Name: ")
        age = eval(input("Enter Age: "))
        strec = [rno, name, age]
        p.dump(strec, f)
        ch = input("Want to enter more records? (y/n): ")
    print("Records added to the file successfully...")
    f.close()
    
def load15():
    f = open("student1.dat", "rb")
    try:
        print("{0:^10}{1:<20}{2:>8}".format("R. No.", "Name", "Age"))
        print("========================")
        while True:
            rno, name, age = p.load(f)
            if age > 15:
                print("{0:^10}{1:<20}{2:>8}".format(rno, name, age))
    except EOFError:
        pass

ch = 'y'
while ch == 'y':
    print("-----------------------")
    print("          Menu            ")
    print("-----------------------")
    print("1. Create File and Add Records")
    print("2. Display records with age more than 15")
    c = eval(input("Enter your choice: "))
    if c == 1:
        dump()
    elif c == 2:
        load15()
    else:
        print("Invalid choice")
    ch = input("Continue? (y/n): ")
