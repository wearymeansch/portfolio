import random

word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо',
             'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила',
             'конец',
             'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги', 'земля', 'машина', 'вода', 'отец',
             'проблема', 'час', 'право', 'нога', 'решение', 'дверь', 'образ', 'история', 'власть', 'закон', 'война',
             'бог', 'голос', 'тысяча', 'книга', 'возможность', 'результат', 'ночь', 'стол', 'имя', 'область', 'статья',
             'число', 'компания', 'народ', 'жена', 'группа', 'развитие', 'процесс', 'суд', 'условие', 'средство',
             'начало', 'свет', 'пора', 'путь', 'душа', 'уровень', 'форма', 'связь', 'минута', 'улица', 'вечер',
             'качество', 'мысль', 'дорога']

##def get_word():
##    word = random.choice(word_list)
##    return word

def get_word():
    return random.choice(word_list).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play():
    word = get_word()
    word = word.upper()
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)
    print('Введите букву или слово')
    print(word)
    j = list(word)
    q = list(word_completion)
    while tries!=0:
        #print(word)
        a = input()
        if a.isalpha():
            a = a.upper()
        else:
            print('Введите букву')
            continue
        if len(a)==1:
            if a not in guessed_letters:
                guessed_letters.append(a)
                ##print(guessed_letters)
            else:
                print('Вы уже вводили эту букву')
                print(''.join(word_completion))
                #print(guessed_letters)
                continue

            if a in word:
                j = list(word)
                q = list(word_completion)
                for i in range(len(j)):
                    if word[i] == a:
                        q[i] = a
                print("".join(q))
                word_completion = "".join(q)
                print('Осталось попыток', tries)
                #print(word_completion)
                if word == word_completion:
                    print('Вы выиграли')
                    print('Буквы:', ' '.join(guessed_letters), 'Слова', ' '.join(guessed_words))
                    break
                else:
                    continue
            else:
                tries-=1
                print(word_completion)
                print(display_hangman(tries))
                print('осталось попыток', tries)
                continue

        if len(a) > 1:
            if a not in guessed_words:
                guessed_words.append(a)
                ##print(guessed_words)
            else:
                print('Вы уже вводили это слово')
                ##print(guessed_words)
                continue

        if a == word:
            print('Вы выиграли')
            print('Буквы:', ' '.join(guessed_letters), 'Слова', ' '.join(guessed_words))
            break
        else:
            tries-=1
            print(tries)
            print(display_hangman(tries))
            continue
    if tries == 0:
        print('Вы проиграли', 'загаданное слово:', word)
        print('Буквы:', ' '.join(guessed_letters), 'Слова', ' '.join(guessed_words))



while True:
    play()
    print('Ещё раз?')
    s = input()
    if s == 'д':
        print('')
    else:
        break
