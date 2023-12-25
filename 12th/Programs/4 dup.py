def dup(list1):
    oglen = len(list1)
    for i in range(oglen):
        list1.append(list1[i])

oglist = eval(input("Enter list: "))
print("Original List:", oglist)
dup(oglist)
print("List with duplicated elements:", oglist)
