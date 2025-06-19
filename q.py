k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
left = []
right = [0]*len(a)
for i in range(len(a)):
    left.append(i-1)
    while left[i]>=0 and a[left[i]]>a[i]:
        left[i]==left[left[i]]

for i in range(len(a)-1,-1,-1):
    right[i]=i+1
    while right[i] < len(a) and a[right[i]] >= a[i]:
        right[i] = right[right[i]]
for i in range(len(a)):
    r = a[i]*(i-left[i])*(right[i]-i)
    print(r)
print(left, right)
