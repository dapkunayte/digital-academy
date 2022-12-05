import junior
import junior_part_7 as jp7
import junior_part_8 as jp8
import junior_part_9 as jp9

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Результат умножения чисел: ", junior.multiply(999))
    print("Перевернутое число: ", junior.reverse(156384741))
    print("Есть ли три слова подряд: ", junior.three_words("ab ab ab 4"))
    print("Результат замены: ", junior.left_replace(["bright", "alright", "ok"]))
    print("Значение медианы: ", junior.mean([3, 6, 20, 99, 10, 15]))
    print("Количество 'полосатых' слов: ", junior.striped_word("Dog,cat,mouse,bird.Human."))

    # Крестики-нолики
    data = [
        "OOX",
        "XOO",
        "OXO"
    ]
    print("Победитель: ", jp7.cross_zero(data))

    # Шифратор
    crypt = (('X...',
              '..X.',
              'X..X',
              '....'),
             ('itdf',
              'gdce',
              'aton',
              'qrdi'))
    print(jp8.decrypter(crypt))

    # возраст приведений
    print("Возраст приведения", jp8.ghost_age(9990))

    # примеры максимума и минимума
    print(jp9.minimum(3, 2))
    print(jp9.maximum(3, 2))

    print(jp9.minimum([1, 2, 0, 3, 4]))
    print(jp9.maximum([1, 2, 0, 3, 4]))

    print(jp9.minimum("hello"))
    print(jp9.maximum("hello"))

    print(jp9.minimum(2.2, 5.6, 5.9, key=int))
    print(jp9.maximum(2.2, 5.6, 5.9, key=int))

    print(jp9.minimum([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))
    print(jp9.maximum([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))

    print(jp9.maximum("hello", key=int))
    print(jp9.maximum(1))

    set_pawns_1 = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
    set_pawns_2 = {"b4", "c4", "d4", "e4", "f4", "g4", "e5"}
    print(jp9.pawns(set_pawns_1))
    print(jp9.pawns(set_pawns_2))
