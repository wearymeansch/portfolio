n = int(input())
c = [0]*10
k=0
for i in range(n):
    b = input()
    good=True
    for i in range(len(b)-1):
        if b[i]>b[i+1]:
            good=False
            break
    if good:
        perc=int(b[0])
        k+=sum(c[:perc+1])
        posc=int(b[-1])
        c[posc]+=1
print(k)    
