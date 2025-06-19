a = int(input())
c = []
for i in range(a):
    b = input()
    good=True
    for i in range(len(b)-1):
        if b[i]>b[i+1]:
            good=False
            break
    if good:
        c.append(b)
k=0
for i in range(len(c)):
    for j in range(i+1,len(c)):
        if c[i][-1]<=c[j][0]:
            k+=1
print(k)    
