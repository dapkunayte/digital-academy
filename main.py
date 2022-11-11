import junior

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Результат умножения чисел: ", junior.multiply(999))
    print("Перевернутое число: ", junior.reverse(156384741))
    print("Есть ли три слова подряд: ", junior.three_words("ab ab ab 4"))
    print("Результат замены: ", junior.left_replace(["bright aright", "ok"]))
    print("Значение медианы: ", junior.mean([3, 6, 20, 99, 10, 15]))
    print("Количество 'полосатых' слов: ", junior.striped_word("Dog,cat,mouse,bird.Human."))


