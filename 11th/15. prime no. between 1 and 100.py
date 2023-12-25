for j in range(2, 101):
    n=j
    for i in range(2, n):
        if n%i==0:
            break
    else:
        print(n)

