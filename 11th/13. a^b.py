b=eval(input('Enter value for base: '))
p=eval(input('Enter value for power: '))
f=1

for i in  range(1, p+1):
    f=f*b
else:
    print(b, '^', p, '=', f)

