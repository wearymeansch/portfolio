n,x = [int(i) for i in input().split()]
a = [(int(i),j+1) for i,j in zip(input().split(),range(n))]
sp=a[-1][0]
a.sort()
b = []
nd = 0
while x<=sp:
    if nd+1<len(a):
        while a[nd+1][0]<x:
            nd+=1
    if a[nd][0]>=x:
        nd-=1
    if nd==-1:
        break
    b.append(a[nd][1])
    x+=a[nd][0]
    a.pop(nd)
if x>sp:
    x+=sp
    b.append(sp)
    print(len(b))
    print(*b)
else:
    print(0)
