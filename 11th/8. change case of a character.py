c=input('Enter a character: ')
ch=ord(c)

if ch>=65 and ch<=90:
    ch=ch+32
elif ch>=97 and ch<=122:
    ch=ch-32
else:
    print('Invalid character')

c=chr(ch)
print('Changed case:', c)

