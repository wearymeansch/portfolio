n,x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
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
if x>a[-1]:
    x+=a[-1]
    a[-1]=0
    b.append(n)
    print(len(b))
    print(*b)
else:
    print(0)
