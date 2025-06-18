import random

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password
    
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

print('Введите количество паролей для генерации')
a = int(input())
print('Введите длину одного пароля')
b = int(input())
print('Включать ли цифры 0123456789? y/n')
c = input()
if c == 'y':
    chars += digits
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? y/n')
d = input()
if d == 'y':
    chars += uppercase_letters
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? y/n')
e = input()
if e == 'y':
    chars += lowercase_letters
print('Включать ли символы !#$%&*+-=?@^_? y/n')
f = input()
if f == 'y':
    chars += punctuation
print('Исключать ли неоднозначные символы il1Lo0O? y/n')
g = input()
if g == 'y':
    for i in 'il1Lo0O':
        chars = chars.replace(i,'')
for i in range(a):
    print(generate_password(b, chars))
