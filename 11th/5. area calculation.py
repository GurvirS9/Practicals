print('Area Calculation')
print('1.Rectangle')
print('2.Circle')
print('3.Square')
print('4.Triangle')
ch=eval(input('Enter Your Choice (1-4): '))

if ch==1:
        l=eval(input('Enter Length: '))
        b=eval(input('Enter Breadth: '))
        a=l*b
        print('Area of rectangle is', a)
        
elif ch==2:
    r=eval(input('Enter Radius: '))
    a=3.14*r**2
    print('Area of circle is', a)
    
elif ch==3:
    s=int(input('Enter Side:'))
    a=s**2
    print('Area of square is',a)
    
elif ch==4:
    h=eval(input('Enter Height: '))
    b=eval(input('Enter Base: '))
    a=0.5*b*h
    print('Area of rectangle',a)
    
