def view():
    myfile = open("para.txt", "r")
    print("File contents:")
    print()
    for line in myfile:
        for ch in line:
            print(ch, end='')
    print("\n")
    myfile.close()

def char():
    d={}
    myfile = open("para.txt", "r")
    data = myfile.read()
    for ch in data:
        if ch not in d:
            d[ch] = data.count(ch)
    for key, value in d.items():
        print(key, ":", value)

def word():
    d={}
    myfile = open("para.txt", "r")
    data = myfile.read()
    words = data.split()
    for word in words:
        if word not in d:
            d[word] = data.count(word)
    for key, value in d.items():
        print(key, ":", value)

c = 'y'
while c == 'y':
    print("-------------MENU-------------")
    print("1. View file contents")
    print("2. Count characters")
    print("3. Count words")
    print("4. Exit")
    ch = eval(input("Enter choice: "))
    if ch == 1:
        view()
    elif ch == 2:
        char()
    elif ch == 3:
        word()
    else:
        print("Enter choice (1-4):")
    c = input("Want to continue? (y/n): ")
