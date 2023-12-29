def dup(list1):
    oglen = len(list1)
    list2 = []
    for i in range(oglen):
        if list1[i] not in list2:
            list2.append(list1[i])
    else:
        return list2

oglist = eval(input("Enter list: "))
print("Original List:", oglist)
undup = dup(oglist)
print("List w/o duplicated elements:", undup)
