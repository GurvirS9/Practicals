y=int(input('Enter years: '))
m=int(input('Enter months in number: '))

if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    print('31 days')
elif m==4 or m==6 or m==9 or m==11:
    print('30 days')
elif m==2:
    if (y%4==0 and y%100!=0) or (y%100==0 and y%400==0):
        print('29 days')
    else:
        print('28 days')

