n=int(input('Enter number of terms you want: '))
print('0')
print('1')
a, b = 0, 1

for i in range(3, n+1):
    c=a+b
    a=b
    b=c
    print(c)

