a = int(input())
b = int(input())
besti = 0 #лучшее число
bests = 0 #лучшая сумма
for i in range(a,b+1):
    s = 0 #очередная сумма
    for j in range(1,i+1):
        if i % j == 0:
##            print(j)
            s += j
    print(i, ':', s)
    if s >= bests:
        bests = s
        besti = i
print(besti, bests)
