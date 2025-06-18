kp = 0
for a in range(1, 151):
    print(a)
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                for e in range(max(a,b,c,d)+1, 151):
                    kp += 1
                    l = a**5+b**5+c**5+d**5
                    r = e**5
                    if l==r:
                        print(a,b,c,d,e, a+b+c+d+e)
                        break
                    elif l<r:
                        break
print(kp)                        
