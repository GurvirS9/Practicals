div=eval(input('Enter number: '))
dir=eval(input('Enter number: '))

r=div%dir

while r!=0:
    div=dir
    dir=r
    r=div%dir
else:
    print('HCF =', dir)

