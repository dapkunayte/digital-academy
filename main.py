import junior

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Результат умножения чисел: ",junior.multiply(999))
    print("Перевернутое число: ", junior.reverse(1563847412))
    print("Есть ли три слова подряд: ",junior.threeWords("1 2 3 4"))
    print("Результат замены: ", junior.leftReplace(["bright aright", "ok"]))
    print("Значение медианы: ",junior.mean([3, 6, 20, 99, 10, 15]))
    print("Количество 'полосатых' слов: ",junior.stripedWord("Dog,cat,mouse,bird.Human."))

