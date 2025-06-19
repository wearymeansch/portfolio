n,s = [int(i) for i in input().split()]
a = [input().split() for i in range(n)]
l = [int(a[0])for i in a]
r = [int(a[1])for i in a]
suml=sum(l)
sumr=sum(r)
for i in range(n):
    sumlo=suml-l[i]
    maxg=s-sumlo
    if r[i]<maxg:
        maxg=r[i]
    sumro=sumr-r[i]
    ming=s-sumro
    if l[i]>ming:
        ming=l[i]
    if ming>maxg:
        otv=0
    else:
        otv=maxg-ming+1
