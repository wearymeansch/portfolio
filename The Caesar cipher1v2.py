alph = 'abcdefghijklmnopqrstuvwxyz'
ralph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alph_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ralph_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def code(text, k, alph, alph_up):
    for a in text:
        if a.lower()==a:
            r=alph
        else:
            r=alph_up
        b = r.find(a)
        if b < 0:
            print(a, end = '')
        else:
            print(r[(b+k)%len(r)], end = '')
    print()

def find_word_en(text, k):
    code(text, k, alph, alph_up)
       
def find_word_ru(text, k):
    code(text, k, ralph, ralph_up)

def de_word_ru(text, k):
    code(text, -k, ralph, ralph_up)

def de_word_en(text, k):
    code(text, -k, alph, alph_up)

                
while True:
    print('Выбери шифрование или дешифрование (ш/д)')
    n = input()
    print('Выбери язык: русский или английский (р/а)')
    a = input()
    print('Введи ключ (натуральное число)')
    k = int(input())
    print('Введи текст')
    text = input()
    if a == 'р' and n == 'ш':
        find_word_ru(text, k)
    elif a == 'а' and n == 'ш':
        find_word_en(text, k)
    elif a == 'а' and n == 'д':
        de_word_en(text, k)
    elif a == 'р' and n == 'д':
        de_word_ru(text, k)
    print('Ввести текст еще раз? (д/н)')
    d = input()
    if d == 'д':
        continue
    else:
        break
print('пока')





##while True:
##    print('Выберите шаифрование или дешифрование ш/д')
##    v = input()
##    print('Выберите язык')
##    r = input()
##    print('Введите текст')
##    text = input()
##    print('Выберите ключ')
##    K = int(input())
##    if v == 'ш' and r == 'р':
##        find_word(text, k)
##        break
##print('пока')
##
##
        
##print(len(ralph))
##print(len(alph))
##def findrqw_word(text, k):
##    for i in range(len(ralph)):
##        if text[i].lower()==text[i]:
##            a = text[i]
##            b = int(ralph.find(a))
##            if b < 0:
##                l = text[i]
##                print(l, end = '')
####            elif b+k == 31:
####                print('я', end='')
####            elif b+k > 31:
####                print(ralph[((b+k)%31)-1], end = '')
##            else:
##                print(ralph[(b+k)%31], end = '')

##print('Введите текст')
##text = input()
##print('Введите ключ')
##k = int(input())
##find_word(text, k)
