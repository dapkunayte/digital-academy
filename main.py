import junior
import junior_part_7 as jp7
import junior_part_8 as jp8

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
    print(jp8.ghost_age(9995))


