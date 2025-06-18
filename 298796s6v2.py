n = int(input())
s = 0
p = 1
for i in range(1, n+1): # перебор всех слагаемых вида i!
    p = i*p
    s += p
print(s)
