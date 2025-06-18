import random
def is_valid(n):
    return n.isdigit() and 1<=int(n)<=b
def is_validb(n):
    return n.isdigit() and 1<=int(n)
print('Добро пожаловать в числовую угадайку')
while True:
    b = input('Введите правую границу для загадавыаемого числа ')
    if is_validb(b):
        b = int(b)
    else:
        continue
    n=random.randint(1, b)
    print('Введите число от 1 до', b)
    kpu = 0
    kpv = 0
    while True:
        num = input()
        kpv += 1
        if is_valid(num) == True:
            num = int(num)
            kpu += 1
            if num < n:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif num > n:
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!')
                print('Количество попыток ввода:', kpv, 'Количество попыток угадывания:', kpu)
                break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
    print('Хотите играть ещё раз (y/n)?')
    a = input()
    if a!='y':
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        
