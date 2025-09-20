n = int(input())
m = int(input())
if n>m:
    n,m = m,n
rn = (n-1)//2
n = 2 if n%2==0 else 1
m = m-2*rn
print(m*n)
    
