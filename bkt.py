kp = 0
for b in range(11):
    for k in range(21):
        t=100-b-k
        kp += 1
        if 10*b+5*k+0.5*t==100:
            print(b,k,t)
print(kp)
