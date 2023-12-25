n=int(input('How many numbers you want to enter: '))

ec=oc=es=os=0

for c in range(1, n+1):
    num=eval(input('Enter number: '))
    if num%2==0:
        ec=ec+1
        es=es+num
    else:
        oc=oc+1
        os=os+num
else:
    print('Total even count =', ec)
    print('Total odd count =', oc)
    print('Sum of even =', es)
    print('Sum of odd =', os)

