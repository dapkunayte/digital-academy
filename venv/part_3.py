# importing os module
import os

#Решил реализовать функцию так, чтобы использовалось имя учётной записи компьютера
def hello_python_task():
    print("-----Задача Welcome to Python-----")
    name = os.getlogin() #  получение имени учётной записи
    print(f'Hello {name}! You just delved into Python. Great start!\n') # вывод нужного текста

#Функция решения задачи "Заголовок"
def title_task(text):
    print("-----Задача Заголовок-----")
    print("Заголовок:",text.title(),"\n")

#Функция решения задачи "Форматированный вывод денежной суммы"
def amount_format_task(amount):
    print("-----Форматированный вывод денежной суммы-----")
    amount_format = "{:.2f}".format(amount)
    print("Форматированный вывод:",amount_format,"\n")

def python_art(thickness):
    print("-----Python Art----\n")
    c="N"
    if thickness==1 or thickness==0:
        print(c)
    elif thickness>40:
        print("Слишком большая толщина. Может неккоретно отображаться в консоли. Допустимые значения долщины от 0 до 40")
    else:
        # letter N
        for i in range(thickness + 1):
            print((c * (thickness)) + ((c * (thickness - 1)).rjust(thickness + (i - 1))) + (c * thickness).rjust(thickness + (thickness - 1) - (i - 1)))
    print("\n")

def carpet(height,word):
    print("-----Дизайнер ковриков----\n")
    width = height * 3

    for i in range(1, height, 2): #цикл по i с единицы по height с увеличением i на 2 каждую итерацию
        print(("<>" * i).center(width, '+')) # выводим i раз символ и центрируем его по длине width с использованием +

    print(word.center(width, '='))

    for i in range(height - 2, 0, -2): #цикл по i с height-2 до 0 с уменьшением i на 2 каждую итерацию. С height-2 потому, что в прошлом цикле последний раз вывели символ height-2 раз, т.к на height цикл уже закончился
        print(('<>' * i).center(width, '+'))



