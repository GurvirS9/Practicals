c=input('Enter a character: ')
ch=ord(c)

if ch>=65 and ch<=90:
    print('Uppercase character')
elif ch>=97 and ch<=122:
    print('Lowercase character')
elif ch>=48 and ch<=57:
    print('Digit')
else:
    print('Special character')

