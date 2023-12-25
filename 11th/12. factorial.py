n=eval(input('Enter number: '))
f=1

for i in range(n, 1, -1):
    print(i, '*', end=' ')
    f=f*i
else:
    print('1 =', f)
    print('Factorial of', n, '=', f)

