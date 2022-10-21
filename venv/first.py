# importing os module
import os

# using getlogin() returning username

#Решил реализовать функцию так, чтобы использовалось имя учётной записи компьютера
def helloPythonTask():
    name = os.getlogin() #  получение имени учётной записи
    print(f'Hello {name}! You just delved into Python. Great start!') # вывод нужного текста

#Функция решения задачи "Заголовок"
def titleTask(text):
    print(text.title())

#Функция решения задачи "Форматированный вывод денежной суммы"
def amountFormatTask(amount):
    amountFormat = "{:.2f}".format(amount)
    print(amountFormat)