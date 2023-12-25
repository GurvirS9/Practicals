print('Enter first time')
h1=eval(input('Enter Hours: '))
m1=eval(input('Enter Minutes: '))
s1=eval(input('Enter Seconds: '))

print('Enter second time')
h2=eval(input('Enter Hours: '))
m2=eval(input('Enter Minutes: '))
s2=eval(input('Enter Seconds: '))

th=h1+h2
tm=m1+m2
ts=s1+s2

if ts>=60:
    tm=tm+1
    ts=ts-60
if tm>=60:
    th=th+1
    tm=tm-60
    
print(th, 'hrs', tm, 'mins', ts, 'secs')

