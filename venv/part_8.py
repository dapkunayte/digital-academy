# неуникальные элементы
def not_uniq_elements(number_list) -> list:
    not_uniq = [x for x in number_list if number_list.count(x) >= 2]
    return not_uniq

# перестановки
def my_permutations(x, y, z, n):
    list_x, list_y, list_z = list(range(x+1)), list(range(y+1)), list(range(z+1))
    result = [[x, y, z]
              for x in list_x
              for y in list_y
              # не уверен, что можно решить с меньшей вложенностью
              for z in list_z
              if x + y + z != n]
    return result

# удвоенные нечётные
def sqr_odd_numbers(n) -> list:
    sqr_odd_list = [x*2 for x in range(n) if x % 2 != 0]
    return sqr_odd_list
