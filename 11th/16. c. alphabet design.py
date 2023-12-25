"""
to print:
A
B B
C C C
D D D D
E E E E E
"""

for i in range(65, 70):
    for j in range(65, i+1):
        print(chr(i), end=' ')
    else:
        print('')

