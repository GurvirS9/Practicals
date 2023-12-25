n=eval(input('Enter number: '))
r=sum=0
org=n

while n>0:
    r=n%10
    sum=sum+(r*r*r)
    n=n//10
else:
    if (org == sum):
        print('Yes,', org, 'is an Armstrong number')
    else:
        print('No,', org, 'is not an Armstrong number')

