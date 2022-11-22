import part_8

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # не уникальные элементы
    number_list = [10, 9, 10, 10, 9, 8]
    print(part_8.not_uniq_elements(number_list))

    # перестановки
    x, y, z, n = 1, 1, 1, 2
    print(part_8.my_permutations(x, y, z, n))

    # удвоенные нечётные
    n = 5
    print(part_8.sqr_odd_numbers(n))