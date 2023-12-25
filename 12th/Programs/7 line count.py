def lcount():
    data = open("para.txt","r")
    lc = 0
    for line in data:
        if word.lower() in line.lower():
            lc += 1
    print("No of lines containing the word '", word, "' =", lc)

word = input("Enter a word to search: ")
lcount()
