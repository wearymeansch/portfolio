#birds = 5000   # глобальная переменная

def print_texas():
    if birds<5000:
        return# делаем возрат из функции, чтобы малое количество птиц не печаталось
    print('В Техасе обитает', birds, 'птиц.')

def print_california():
    print('В Калифорнии обитает', birds, 'птиц.')
    
birds_tex=1000
birds_cal=7000
birds=birds_tex
print_texas()
birds=birds_cal
print_california()
