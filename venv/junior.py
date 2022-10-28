import math
#Задача Произведение цифр
def multiply(num)->int:
    if type(num)!=int:
        print('получено не число')
        return 0
    strNum = str(num)
    strNum = strNum.strip('0')
    res = 1
    for i in strNum:
        res*=int(i)
    return res

# Число "наоборот" (усложненное)
def reverse(num)->int:
    strNum = str(num)
    if strNum[len(strNum)-1]=="0" and len(strNum)>1:  # обрабатываем последний 0, чтобы исключить его из решения
        strNum = strNum[:len(strNum)-1]
    if strNum[0]=="-":  # обрабатываем минус
        strNum = strNum[0] + strNum[1:][::-1] # прибавляем "-" после чего прибавляем перевернутую часть строки без минуса
    else:
        strNum = strNum[::-1] # переварачиваем строку

    if int(strNum)>=(2**31)-1 or int(strNum)<=-(2**31): #обрабатываем граничные условия
        return 0
    else:
        return int(strNum)

#Три слова
def threeWords(string)->bool:
    strSplit = string.split(sep=' ')
    k = 0
    for i in strSplit:
        if i.isdigit():
            k=0
        else:
            k+=1

    if k>=3:
        return True
    else:
        return False

# Мир захватили левши
def leftReplace(list):
    for i in range(len(list)): # цикл с индексом по элементам списка
        if "right" in list[i]: # если right входит в элемент списка по индексу
            list[i] = list[i].replace("right","left") # выполняем замену
    return list

# Медиана
def mean(list)->float:
    list = sorted(list)
    if len(list)%2!=0: # если количество элементов нечетное
        return list[math.ceil(len(list)/2)] # возвращаем элемент списка, который находится посередине : определяем индекс путем деления длины на 2 и округлением до целого
    else:
        return (list[int((len(list)/2))]+list[int((len(list)/2)-1)])/2 # возвращаем среднее между элементами списка с иднексами длинны массива, деленого на 2, и предыдщуего относительно него

def stripedWord(string):
    strList = string.split(" ")
