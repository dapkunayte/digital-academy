import random as rnd

def sumOfThreeRandNum():
    print("-----Задача Среднее-----")
    a,b,c = rnd.randint(1, 100),rnd.randint(1, 100),rnd.randint(1, 100)
    sum = (a+b+c)/3
    print(f'Сумма трех: {sum:.2f}\n')

#Решил реализовать так, чтобы обязательно делилось большее число на меньшее
def division():
    print("-----Задача Деление и еще раз деление-----")
    a,b = rnd.randint(1, 100),rnd.randint(1, 100)
    if a>b:
       print("div:",a//b," mod:",a%b,"\n")
    else:
       print("div:",b//a," mod:",b%a,"\n")

#задача по округлению
def rounding(num):
    print("-----Задача Округление-----")
    print(f'Округление до двух: {num:.2f}')
    print(f'Округлене до целого: {num:.0f}')
    print(f'До 11 знаков: {num:=011}\n')