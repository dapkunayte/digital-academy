import part_7

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # анализ текста
    words_popularity, letters_popularity = part_7.popularity_count("hello, word of word")
    print("Подсчет слов: ", words_popularity, " \nПодсчёт букв : ", letters_popularity,"\n")

    # ленивый спекулянт
    rates = {'Sberbank': 55.8, 'VTB24': 53.91, 'ROSBANK': 53.91}
    best_banks = part_7.lazy_trader(rates)
    print("Наиболее выгодное предложение:")
    for key, value in best_banks.items():
        print(key, value, sep=" -> ", end="\n")

    # вверх дном
    book = {'Petr': '546810', 'Katya': '241815'}
    print("\nИнвертированный словарь:", part_7.reverse_dict(book),"\n")

    #Структурируем данные
    dates = ['2017-03-01', '2017-03-02']
    rates = [55.7, 55.2]
    print("Значение курса на дату:", part_7.merge_lists(dates,rates))

    #Римские цифры
    num = 60
    print("\nЧисло ",num, " в римском формате: ", part_7.int_to_roman(num))


