def char(data):
    d = {}
    for ch in data:
        if ch not in d:
            d[ch] = data.count(ch)
    for key, value in d.items():
        print(key, ":", value)

def word(data):
    d = {}
    words = data.split()
    for word in words:
        if word not in d:
            d[word] = words.count(word)
    for key, value in d.items():
        print(key, ":", value)

c = 'y'
while c == 'y':
    print("-------------MENU-------------")
    print("1. Count characters")
    print("2. Count words")
    ch = eval(input("Enter choice: "))
    if ch == 1:
        line = input("Enter a sentence: ")
        char(line)
    elif ch == 2:
        line = input("Enter a sentence: ")
        word(line)
    else:
        print("Invalid choice")
    c = input("Want to continue? (y/n): ")
