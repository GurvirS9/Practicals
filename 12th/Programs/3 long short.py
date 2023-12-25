def view():
    data = open("para.txt", "r")
    print("File contents:")
    print()
    for line in data:
        for ch in line:
            print(ch, end='')
    print("\n")
    data.close()

def long():
    data = open("para.txt", "r")
    longest = ""
    maxlen = 0 
    for line in data:
        w = line.split()
        for word in w:
            wordlen = len(word)
            if wordlen > maxlen:
                longest = word
                maxlen = wordlen
    print("Longest word is '", longest, "' with length :", maxlen)

def short():
    data = open("para.txt", "r")
    shortest = ""
    minlen = 50
    for line in data:
        w = line.split()
        for word in w:
            wordlen = len(word)
            if wordlen < minlen:
                shortest = word
                minlen = wordlen
    print("Shortest word is '", shortest, "' with length :", minlen)

c = 'y'
while c == "y":   
    print("-------------MENU-------------")
    print("1. View contents")
    print("2. Longest word")
    print("3. Shortest word")
    ch = eval(input("Enter choice: "))
    if ch == 1:
        view()
    elif ch == 2:
        long()
    elif ch == 3:
        short()
    else:
        print("Invalid")
    c = input("Want to continue? (y/n): ")
