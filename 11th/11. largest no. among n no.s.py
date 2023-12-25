n=int(input('How many numbers you want to enter: '))
m=0

for c in range(1, n + 1):
    num=eval(input('Enter number: '))
    if c==1:
        m=num
    else:
        if num>m:
            m=num
else:
    print('Largest number =', m)

