n=eval(input('Enter number: '))
t=int(input('Enter number of terms: '))
p=1

for i in range(1, t+1):
    p=n*i
    print(n, '*', i, '=',p)

