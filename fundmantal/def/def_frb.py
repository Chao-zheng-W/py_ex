def frb(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return frb(n-1)+frb(n-2)
print(frb(6))

for i in range(1,7):
    print(frb(i))
