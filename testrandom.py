import random

#random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел

for _ in range(10):
    print(random.randint(1, 100))
numbers = list(range(2, 10, 2)) + [3]

num = random.choice(numbers)
print(numbers,num)
