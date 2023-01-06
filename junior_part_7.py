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