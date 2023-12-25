n=eval(input('Enter number: '))
r=rev=0
org=n

while n>0:
    r=n%10
    rev=(rev*10)+r
    n=n//10
else:
    if (org == rev):
        print(org, 'is a Palindrome')
    else:
        print(org, 'is not a Palindrome')

