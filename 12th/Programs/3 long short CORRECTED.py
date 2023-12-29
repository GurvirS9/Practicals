def long():
    line = input("Enter a sentence: ")
    words = line.split()  
    longest = ""
    maxlen = 0 
    for word in words:
        wordlen = len(word)
        if wordlen > maxlen:
            longest = word
            maxlen = wordlen
    print("Longest word is '", longest, "' with length:", maxlen)

def short():
    line = input("Enter a sentence: ")
    words = line.split()  
    shortest = ""
    minlen = 50
    for word in words:
        wordlen = len(word)
        if wordlen < minlen:
            shortest = word
            minlen = wordlen
    print("Shortest word is '", shortest, "' with length:", minlen)

c = 'y'
while c == "y":   
    print("-------------MENU-------------")
    print("1. Longest word")
    print("2. Shortest word")
    ch = eval(input("Enter choice: "))
    if ch == 1:
        long()
    elif ch == 2:
        short()
    else:
        print("Invalid choice")
    c = input("Want to continue? (y/n): ")
