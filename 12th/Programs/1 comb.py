def separate(list1, list2):
    combined = list1 + list2
    odd=[]
    even=[]
    for num in combined:
        if num % 2 != 0:
            odd.append(num)
        elif num % 2 == 0:
            even.append(num)
        else:
            break
    result = odd + even
    return result

list1 = eval(input('Enter values for list 1: '))
list2 = eval(input('Enter values for list 2: '))

result = separate(list1, list2)
print("Result List:", result)
