a=eval(input('Enter first number: '))
b=eval(input('Enter second number: '))

if a>b:
    L=a
else:
    L=b
for i in range(L, a*b+1):
    if (i%a==0 and i%b==0):
        print('LCM =', i)
        break


