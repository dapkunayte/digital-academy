# importing os module
import os

# using getlogin() returning username

#Решил реализовать функцию так, чтобы использовалось имя учётной записи компьютера
def helloPythonTask():
    print("-----Задача Welcome to Python-----")
    name = os.getlogin() #  получение имени учётной записи
    print(f'Hello {name}! You just delved into Python. Great start!\n') # вывод нужного текста

#Функция решения задачи "Заголовок"
def titleTask(text):
    print("-----Задача Заголовок-----")
    print("Заголовок:",text.title(),"\n")

#Функция решения задачи "Форматированный вывод денежной суммы"
def amountFormatTask(amount):
    print("-----Форматированный вывод денежной суммы-----")
    amountFormat = "{:.2f}".format(amount)
    print("Форматированный вывод:",amountFormat,"\n")
