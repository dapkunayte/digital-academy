class bcolors: # при помощи этого можно реализовать вывод текста в консоль с другим цветом (использовал FAIL для ошибок) как пример f"{bcolors.FAIL}ValueError: object cant't be used with this key", потом убрал
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def maximum(*variables,key=lambda x: x):
        if len(variables)==1:
            if hasattr(*variables,"__iter__"): # проверка, является ли переданный аргумент (когда он один) итерируемым
                try:
                    variables_dict = {}
                    for variable in list(*variables):
                        if key(variable) not in variables_dict.keys():
                            variables_dict[key(variable)] = variable
                    sorted_variables = sorted(variables_dict.items())
                    len_sorted_variables = len(sorted_variables)-1
                    return sorted_variables[len_sorted_variables][1]
                except ValueError:
                    return f"ValueError: object cant't be used with this key"
            else:
                return f"TypeError: {type(*variables)} object is not iterable"
        else:
            try:
                variables_dict = {}
                for variable in list(variables):
                    if key(variable) not in variables_dict.keys():
                        variables_dict[key(variable)] = variable
                sorted_variables = sorted(variables_dict.items())
                len_sorted_variables = len(sorted_variables) - 1
                return sorted_variables[len_sorted_variables][1]
            except ValueError:
                return f"ValueError: object cant't be used with this key"


def minimum(*variables, key=lambda x: x):
    if len(variables) == 1:
        if hasattr(*variables, "__iter__"):  # проверка, является ли переданный аргумент (когда он один) итерируемым
            try:
                variables_dict = {}
                for variable in list(*variables):
                    if key(variable) not in variables_dict.keys():
                        variables_dict[key(variable)] = variable
                sorted_variables = sorted(variables_dict.items())
                len_sorted_variables = len(sorted_variables) - 1
                return sorted_variables[0][1]
            except ValueError:
                return f"ValueError: object cant't be used with this key"
        else:
            return f"TypeError: {type(*variables)} object is not iterable"
    else:
        try:
            variables_dict = {}
            for variable in list(variables):
                if key(variable) not in variables_dict.keys():
                    variables_dict[key(variable)] = variable
            sorted_variables = sorted(variables_dict.items())
            len_sorted_variables = len(sorted_variables) - 1
            return sorted_variables[0][1]
        except ValueError:
            return f"ValueError: object cant't be used with this key"

def pawns(set_pawns)->int:
    list_pawns = list(set_pawns)
    safe_pawns = [[chr(ord(list(pawn)[0])-1)+str(int(pawn[1])-1), chr(ord(list(pawn)[0])+1)+str(int(pawn[1])-1)] for pawn in list_pawns]
    # chr(ord(list(peshka)[0])-1) при помощи ord получаем численное представление буквы, отнимаем или прибавляем 1 (чтобы получить значение буквы клетки ниже по диагонали)
    # +str(int(peshka[1])-1) после чего прибавляем число, меньшее на 1, чтобы спуститься ниже по шахматной доске
    # таким образом мы генерируем список из списка координат, которые находятся слева и справа по диагонали от каждой из координат исходного списка
    safe_counter = 0
    for safe_pawn in safe_pawns:
        if (safe_pawn[0] in list_pawns) or (safe_pawn[1] in list_pawns): # проверяем, есть ли наши полученные координаты по диагонали в исходном списке, если есть хотя бы одна, то пешка защищена
            safe_counter+=1
    return safe_counter


""" черновик
        a_with_key = a
        if key != None: # если ключ был передан
            try: # попытка применить функцию из ключа на переданный параметр
                a_with_key = [key(x) for x in a_with_key]
            except TypeError:
                return f"{bcolors.FAIL}TypeError: {type(a)} object cant't use with this key" # возврат ошибки, если нельзя применить функцию
        try: # проверка является ли переданный объект итерируемым
            sorted_a = sorted(a_with_key) # по условию sorted не запрещено было использовать
            max_val_index = len(sorted_a)-1
            return sorted_a[max_val_index]
        except TypeError:
            return f"{bcolors.FAIL}TypeError: {type(a)} object is not iterable"
"""
