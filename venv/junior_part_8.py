import math


def decrypter(crypt) -> str:
    grid = crypt[0]
    grid_matrix = []
    for i in range(len(grid)):
        grid_matrix.append(list(grid[i]))

    letters = crypt[1]
    letters_matrix = []
    for i in range(len(letters)):
        letters_matrix.append(list(letters[i]))

    rows_number = len(grid_matrix)
    column_len = len(grid_matrix[0])

    # первая итерация
    first_iter = []
    first_iter = [letters_matrix[i][j] for i in range(rows_number) for j in range(column_len) if grid_matrix[i][j] == 'X']

    # вторая итерация
    second_iter = []
    grid_90_1 = [list(reversed(col)) for col in zip(*grid_matrix)]
    second_iter = [letters_matrix[i][j] for i in range(rows_number) for j in range(column_len) if grid_90_1[i][j] == 'X']

    # третья итерация
    third_iter = []
    grid_90_2 = [list(reversed(col)) for col in zip(*grid_90_1)]
    third_iter = [letters_matrix[i][j] for i in range(rows_number) for j in range(column_len) if grid_90_2[i][j] == 'X']

    # четвертая итерация
    fourth_iter = []
    grid_90_3 = [list(reversed(col)) for col in zip(*grid_90_2)]
    fourth_iter = [letters_matrix[i][j] for i in range(rows_number) for j in range(column_len) if grid_90_3[i][j] == 'X']

    return ''.join(first_iter+second_iter+third_iter+fourth_iter)

# возвраст приведений
def ghost_age(transparency) -> int:
    max_trasparency = 10000
    age = 0
    while transparency != max_trasparency:
        age += 1
        if isFibonacci(p):
            max_trasparency -= p
        else:
            max_trasparency += 1
    return age


# две функции ниже необходимы для проверки, является ли число элементом последовательности фиббоначи
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x

def isFibonacci(n):
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)
