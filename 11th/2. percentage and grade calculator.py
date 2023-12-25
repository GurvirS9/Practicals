p=eval(input('Enter marks for Physics: '))
c=eval(input('Enter marks for Chemistry: '))
m=eval(input('Enter marks for Maths: '))
cs=eval(input('Enter marks for Computer Science: '))
eng=eval(input('Enter marks for English: '))

t=(p+c+m+cs+eng)/500*100
print('Your percentage is', t)

if t>=85 and t<=100:
    print('Your Grade is A')
if t>=75 and t<=84:
    print('Your Grade is B')
if t>=61 and t<=74:
    print('Your Grade is C')
if t>=33 and t<=60:
    print('Your Grade is D')
if t>=0 and t<=32:
    print('Your Grade is F')

