kp = 0
kp2 = 0
for n in range(1, (365-30-31)//28+1):
    for k in range(1, (365-28*n-31)//30+1):
        kp2 += 1
        for m in range(1,(365-28*n-30*k)//31+1):
            kp += 1
            if 28*n+30*k+31*m==365:
                print(n,k,m)
print(kp, kp2)    
