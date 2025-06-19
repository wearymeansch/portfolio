n,k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
s=0
sf=[0]*n
for l in range(n):
    for r in range(l,n):
        sf[r]=a[r]
        if l<r:
            lp=max(r-k,l)
            maxp=max(sf[lp:r])
            sf[r]=min(maxp,sf[r])
            #print(l,r,lp,maxp,sf[r])
        s+=sf[r]
    print(sf[l:])
print(s)
