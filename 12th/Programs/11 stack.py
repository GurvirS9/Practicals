stk = []

def push(stk):
    ch = 'y'
    while ch == 'y':
        print("Enter student data below:-")
        rno = eval(input("Enter Roll No.: "))
        name = input("Enter Name: ")
        marks = eval(input("Enter Marks: "))
        temp = (rno, name, marks)
        stk.append(temp)
        ch = input("Want to enter more records? (y/n): ")

def pop(stk):
    if (len(stk)) == 0:
        print("Stack is empty")
    else:
        print("Popped", stk.pop())

def display(stk):
    if (len(stk)) == 0:
        print("Stack is empty")
    else:
        for i in range(len(stk)):
            print(i+1, "-", stk[i])

ch = 'y'
while ch == 'y':
    print("          MENU           ")
    print("1. Push record")
    print("2. Pop record")
    print("3. Display stack")
    print("4. Exit")
    c = eval(input("Enter choice (1-4): "))
    if c == 1:
        push(stk)
    elif c == 2:
        pop(stk)
    elif c == 3:
        display(stk)
    elif c == 4:
        break
    else:
        print("Invalid choice")
    ch = input("Want to continue? (y/n): ")
        
