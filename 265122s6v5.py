# put your python code here
a = int(input())
mi = 10
ma = 0
while a > 0:
    b = a%10 
    ma=max(ma,b)
    mi=min(mi,b)
    a = a//10
print("Максимальная цифра равна",ma)
print("Минимальная цифра равна",mi)
