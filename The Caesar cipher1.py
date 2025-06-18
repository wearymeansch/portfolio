alph = 'abcdefghijklmnopqrstuvwxyz'
ralph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alph_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ralph_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def findq_word(text, k):
    for i in range(len(text)):
        if text[i].lower()==text[i]:
            a = text[i]
            b = int(alph.find(a))
            if b < 0:
                l = text[i]
                print(l, end = '')
            elif b+k == 25:
                print('z', end='')
            elif b+k > 25:
                print(alph[((b+k)%25)-1], end = '')
            else:
                print(alph[(b+k)%25], end = '')
        elif text[i].upper()==text[i]:
            a = text[i]
            b = int(alph_up.find(a))
            if b < 0:
                l = text[i]
                print(l, end = '')
            elif b+k == 25:
                print('z', end='')
            elif b+k > 25:
                print(alph_up[((b+k)%25)-1], end = '')
            else:
                print(alph_up[(b+k)%25], end = '')

        
def find_word(text, k):
    for i in range(len(text)):
        if text[i].lower()==text[i]:
                a = text[i]
                b = int(ralph.find(a))
                if b < 0:
                    l = text[i]
                    print(l, end = '')
                elif b+k == 31:
                    print('я', end='')
                elif b+k > 31:
                    print(ralph[((b+k)%31)-1], end = '')
                else:
                    print(ralph[(b+k)%31], end = '')
        elif text[i].upper()==text[i]:
                a = text[i]
                b = int(ralph_up.find(a))
                if b < 0:
                    l = text[i]
                    print(l, end = '')
                elif b+k == 31:
                    print('я', end='')
                elif b+k > 31:
                    print(ralph_up[((b+k)%31)-1], end = '')
                else:
                    print(ralph_up[(b+k)%31], end = '')


def de_word_ru(text, k):
    for i in range(len(text)):
        if text[i].lower()==text[i]:
            a = text[i]
            b = int(ralph.find(a))
            if b < 0:
                l = text[i]
                print(l, end = '')
            elif b ==k or b<k:
                print(ralph[(b-k)%31], end = '')
            else:
                print(ralph[(b-k)%31], end = '')
        elif text[i].upper()==text[i]:
            a = text[i]
            b = int(ralph_up.find(a))
            if b < 0:
                l = text[i]
                print(l, end = '')
            elif b==k:
                print(ralph_up[((b-k)%31)-1], end = '')
            elif b<k:
                h = ((b-k)%31)+1
                print(ralph_up[h], end = '')
            elif b>k:
                print(ralph_up[(b-k)%31], end = '')

def de_word_en(text, k):
    for i in range(len(text)):
        if text[i].lower()==text[i]:
            a = text[i]
            b = int(alph.find(a))
            if b < 0:
                l = text[i]
                print(l, end = '')
            elif b == k:
                print(alph[(b-k)%25], end = '')
            else:
                print(alph[((b-k)%25)+1], end = '')
        elif text[i].upper()==text[i]:
            a = text[i]
            b = int(alph_up.find(a))
            if b < 0:
                l = text[i]
                print(l, end = '')
            elif b==k:
                print(alph_up[((b-k)%25)-1], end = '')
            else:
                print(alph_up[((b-k)%25)+1], end = '')

                
while True:
    print('Выбери шифрование или дешифрование (ш/д)')
    n = input()
    print('Выбери язык: русский или английский (р/а)')
    a = input()
    print('Выбери ключ (натуральное число)')
    k = int(input())
    print('Введи текст')
    text = input()
    if a == 'р' and n == 'ш':
        find_word(text, k)
        print(' ')
        print('Ввести текст еще раз?')
        d = input()
        if d == 'да':
            continue
        else:
            break
    elif a == 'а' and n == 'ш':
        findq_word(text, k)
        print(' ')
        print('Ввести текст еще раз?')
        d = input()
        if d == 'да':
            continue
        else:
            break
    elif a == 'а' and n == 'д':
        de_word_en(text, k)
        print(' ')
        print('Ввести текст еще раз?')
        d = input()
        if d == 'да':
            continue
        else:
            break
    elif a == 'р' and n == 'д':
        de_word_ru(text, k)
        print(' ')
        print('Ввести текст еще раз?')
        d = input()
        if d == 'да':
            continue
        else:
            break
print('end')





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
