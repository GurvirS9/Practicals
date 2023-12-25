u=eval(input('Enter units: '))

if u<=100:
    bill=u
elif u>100 and u<=300:
    bill=100+(u-100)*2
elif u>300 and u<=600:
    bill=100+400+(u-300)*3
else:
    bill=100+400+900+(u-600)*3
    
tax=0.10*bill
total=bill+tax
print('Tax =', tax)
print('Total Bill =',total)

