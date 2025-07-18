import sys

def height(r):
    if r==None:
        return 0
    else:
        return max(height(r[1]), height(r[2]))+1
def size(r):
    if r==None:
        return 0
    else:
        return size(r[1])+size(r[2])+1
def make_insert(s,zn):#функция вызывается для вставки в корень s
    n = [zn, None, None, None,"r"]#создаем новый эл-т красного цвета
    insert(s, n)#вставляем его в нужное место дерева
    if s == None:
        s=n
    insert_case1(n)#обеспечиваем поддержание всех свойств дерева
    while s[3]:
        s=s[3]
    return s
def grandparent(s):
    if s[3]:
        return s[3][3]
    else:
        return None
def uncle(s):
    g = grandparent(s)
    if g:
        if s[3]==g[1]:
            return g[2]
        else:
            return g[1]
    else:
        return None
def insert(s,n):#функция вызывается для вставки в произвольное место дерева s
    if s == None:#аналог случая 2 в Википедии
        s=n#создание нового эл-та, который к чему-нибудь будет привязан
    elif s[0]>n[0]:
        if s[1]==None:
            s[1]=n
            n[3]=s
        else:
            insert(s[1], n)#вставка числа в левую ветку
    else:
        if s[2]==None:
            s[2]=n
            n[3]=s
        else:
            insert(s[2], n)#вставка числа в правую ветку
#здесь функция insert является рекурсивной, поскольку она вызывает сама себя. У рекурсивных функций
#обязательно должен быть базовый случай, который вычисляется без обращения функции к самой с:ебе.
#Здесь таким базовым случаем является строчка 3. Базовый случай всегда должен достигаться за конечное
#кол-во вызовов функции, иначе может возникнуть бесконечная рекурсия (программа подвиснет).
#В Питоне для защиты от бесконечной рекурсии сделан контроль количества незавершенных вызовов функции.
#По умолчанию допускается не более 1000 незавершенных вызовов функции. Кол-во незавершенных вызовов
#рекурсивной функции ограничивается из-за того, что каждый незавершенный вызов рекурсивной функции
#требует дополнительной памяти для локальных переменных и ссылки на предыдущий незавершенный
#вызов функции, в какое место функции нужно возвращаться.
#В питоне при необходимости можно увеличить максимально допустимое кол-во незавершенных рекурсивных
#вызовов, используя функцию setcursionlimit из модуля sys. Узнать текущую глубину рекурсии можно
#функцией getrecursionlimit
def rotateleft(r):#поворот влево. r - это эл-т, который условно считается старым корнем, а новым корнем
#станет его правый ребёнок 
    if r!= None and r[2] != None:#проверяем, что есть корень и его правый ребёнок, иначе оставляем дерево неизменным
        nr=r[2]#запоминаем ссылку на новый корень
        r[2]=nr[1]#бывший левый ребёнок нового корня станет правым ребёнком старого корня 
        nr[1]=r#левым ребёнком нового корня станет старый корень
        r=nr#исправляем ссылку r на новый корень
    return r
def rotateright(r):#поворот вправо. r - это эл-т, который условно считается старым корнем, а новым корнем
#станет его левый ребёнок 
    if r!= None and r[1] != None:#проверяем, что есть корень и его левый ребёнок, иначе оставляем дерево неизменным
        nr=r[1]#запоминаем ссылку на новый корень
        r[1]=nr[2]#бывший правый ребёнок нового корня станет левым ребёнком старого корня 
        nr[2]=r#правым ребёнком нового корня станет старый корень
        r=nr#исправляем ссылку r на новый корень
    return r

def insert_case1(n):
    if n[3]==None:
        n[4]='b'
    else:
        insert_case2(n)
def insert_case2(n):
    if n[3][4]=='b':
        return
    else:
        insert_case3(n)
def insert_case3(n):
    u = uncle(n)
    if u and u[4]=='r':
        n[3][4]='b'
        u[4]='b'
        g = grandparent(n)
        g[4]='r'
        insert_case1(g)
    else:
        insert_case4(n)
def insert_case4(n):
    g = grandparent(n)
    if n==n[3][2] and n[3]==g[1]:
        rotateleft(n[3])
        n = n[1]
    elif n==n[3][1] and n[3]==g[2]:
        rotateright(n[3])
        n = n[2]
    insert_case5(n)
def insert_case5(n):
    g = grandparent(n)
    n[3][4]='b'
    g[4]='r'
    if n == n[3][1] and n[3]==g[1]:
        rotateright(g)
    else:
        rotateleft(g)
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
s=None
ch = list(range(1,11))# [4,2,8,1,3,6,9,5,7,10]
for ch1 in ch:
    #ch1=int(input())
    s=make_insert(s, ch1)
    print(s)
    print(height(s), size(s))
##s=rotateleft(s)
##print(s)
##print(height(s), size(s))
##s[2]=rotateleft(s[2])
##print(s)
##print(height(s), size(s))
##s[2][2]=rotateleft(s[2][2])
##print(s)
##print(height(s), size(s))
##s[2][2][2]=rotateleft(s[2][2][2])
##print(s)
##print(height(s), size(s))
##s=rotateleft(s)
##print(s)
##print(height(s), size(s))
##s[2]=rotateleft(s[2])
##print(s)
##print(height(s), size(s))
