s=int(input('Enter time in seconds: '))

h=(s//3600)
R=(s%3600)
m=(R//60)
s=(m%60)

print(h, 'hrs', m, 'mins', s, 'secs')

