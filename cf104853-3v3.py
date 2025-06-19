n,x = [int(i) for i in input().split()]
x1 = x
a = [(int(i),j+1) for i,j in zip(input().split(),range(n))]
a1 = [i[0] for i in a]
sp=a[-1][0]
#print("abracadabra")
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
x=x1
b1=b
a = a1
b = []
while x<=a[-1]:
    #print('while')
    imax=-1
    for i in range(len(a)):
        #print('i=', i, a[i]!=0 , a[i]<x , (imax==-1 or a[i]>a[imax]))
        if (a[i]!=0) and (a[i]<x) and (imax==-1 or a[i]>a[imax]):
            #print('if')
            imax=i
            #print(imax)
    #print(b, imax, a[imax], x)
    if imax!=-1:
        x+=a[imax]
        b.append(imax+1)
        a[imax]=0
    else:
        break
if b!=b1:
    xxx=1/0
elif x>a[-1]:
    x+=a[-1]
    a[-1]=0
    b.append(n)
    print(len(b))
    print(*b)
else:
    print(0)

