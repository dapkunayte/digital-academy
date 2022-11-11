import math
import re
import string

#Задача Произведение цифр
def multiply(num)->int:
    if type(num)!=int:
        print('получено не число')
        return 0
    str_num = str(num)
    str_num = str_num.strip('0')
    result = 1
    for i in str_num:
        result*=int(i)
    return result

# Число "наоборот" (усложненное)
def reverse(num)->int:
    str_num = str(num)
    len_num = len(str_num) # длина строки
    if str_num[len_num-1]=="0" and len_num>1:  # обрабатываем последний 0, чтобы исключить его из решения
        str_num = str_num[:len_num-1]
    if str_num[0]=="-":  # обрабатываем минус
        str_num = str_num[0] + str_num[1:][::-1] # прибавляем "-" после чего прибавляем перевернутую часть строки без минуса
    else:
        str_num = str_num[::-1] # переварачиваем строку

    max_int = (2**31)-1
    min_int = -(2**31)

    if int(str_num) >= max_int or int(str_num) <= min_int: #обрабатываем граничные условия
        return 0
    else:
        return int(str_num)

#Три слова
def three_words(string)->bool:
    str_split = string.split(sep=' ')
    words_counter = 0
    for i in str_split:
        if words_counter>=3:
            return True
            break
        elif i.isdigit():
            words_counter=0
        else:
            words_counter+=1

    if words_counter<=3:
        return False

# Мир захватили левши
def left_replace(words):
    len_words = len(words)
    for i in range(len_words): # цикл с индексом по элементам списка
        if "right" in words[i]: # если right входит в элемент списка по индексу
            words[i] = words[i].replace("right","left") # выполняем замену
    return words

# Медиана
def mean(numbers)->float:
    numbers = sorted(numbers)
    len_numbers = len(numbers)
    if len_numbers %2!=0: # если количество элементов нечетное
        mean_index = math.ceil(len_numbers/2) # серидина списка
        return numbers[mean_index] # возвращаем элемент списка, который находится посередине : определяем индекс путем деления длины на 2 и округлением до целого
    else:
        mean_index_1 = int((len_numbers/2))
        mean_index_2 = int((len_numbers /2)-1)
        return (numbers[mean_index_1 ]+numbers[mean_index_2])/2 # возвращаем среднее между элементами списка с иднексами длинны массива, деленого на 2, и предыдщуего относительно него

# Полосатые слова
def striped_word(s):
    s_without_punct = re.sub(r'[^\w\s]', ' ', s)  # удаление пунктуации (удаляем все, кроме буквенных символов и пробелов)
    words = 0
    str_arr = s_without_punct.split(" ")
    for i in str_arr:
        # поиск: если длина слова больше 1 и слово не попадает под регулярное выражение, то мы прибавляем количество "полосатых слов". Регулярка смотрит наличие двух согласных или гласных подряд. Если их нет, то условие выполняется
        if len(i)>1 and not(re.search(r"[BCDFGHJKLMNPQRSTVWXZ]{2,}|[AEIOUY]{2,}",i,re.IGNORECASE)):
            words+=1
    return words

# Крестики нолики

def cross_zero(data):
    x_win = False
    o_win = False

    # перевод исходных данных в двумерный массив
    data_matrix = []
    for i in range(len(data)):
        data_matrix.append(list(data[i]))

    diag_main = [data_matrix[0][0],data_matrix[1][1],data_matrix[2][2]] # главная диагональ матрица
    diag_secondary = [data_matrix[0][2],data_matrix[1][1],data_matrix[2][0]] # побочная диагональ матрица

    if diag_main.count("X")==3:
        x_win = True
    elif diag_main.count("O")==3:
        o_win = True

    if diag_secondary.count("X") == 3:
        x_win = True
    elif diag_secondary.count("O") == 3:
        o_win = True


    # проверка по строкам
    for row in data_matrix:
        if row.count("X")==3:
            x_win = True
        elif row.count("O")==3:
            o_win = True

    # проверка по столбцам
    for column in zip(*data_matrix): # zip(*data_matrix) позволяет получить транспонированную матрицу
        if column.count("X") == 3:
            x_win = True
        elif column.count("O") == 3:
            o_win = True

    if x_win:
        return "X"
    elif o_win:
        return "O"
    else:
        return "D"





