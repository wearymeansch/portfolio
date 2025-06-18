kp = 0
for b in range(101):
    for k in range(101):
        for t in range(101):
            kp += 1
            if 10*b+5*k+0.5*t==100 and b+k+t==100:
                print(b,k,t)
print(kp)
