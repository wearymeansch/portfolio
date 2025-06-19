a = int(input())
b = int(input())
k = int(input())
if a<b:
    r = b-a
    if k>r:
        a+=r
        k-=r
    else:
        a+=k
        k=0
elif b<a:
    r = a-b
    if k>r:
        b+=r
        k-=r
    else:
        b+=k
        k=0
if k%2==0:
    a+=k//2
    b+=k//2
else:
    a+=k//2
    b+=(k//2)+1
print(a,b)
