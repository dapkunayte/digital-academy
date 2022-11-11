import string

# Анализ текста. Популярность
def popularity_count(text)->(dict,dict):

    text_processing = text.translate(str.maketrans('', '', string.punctuation)) # удаление знаков препинания

    words = text_processing.split(" ") # получение списка из слов
    letters = text_processing.replace(" ","") # получение строки букв

    # объявление словарей
    words_popularity = {}
    letters_popularity = {}

    for word in set(words): # в цикле по уникальным словам (set позволяет получить уникальные элементы)
        words_popularity[word] = text.count(word) # подсчитываем количество слов с оригинальной строке

    for letter in set(letters): # в цикле по уникальным буквам (set позволяет получить уникальные элементы)
        letters_popularity[letter] = text.count(letter) # подсчитываем количество букв в оргинальной строке

    return words_popularity,letters_popularity

# Ленивый спекулянт
def lazy_trader(rates)->dict:
    min_value = min(rates.values()) # получение минимального значения в словаре
    best_banks = {} # объявление словаря банков

    for key in rates:
        if rates[key] == min_value: # если у банка значение акции совпадает с минимальным
            best_banks[key] = min_value # добавляем в словарь этот банк

    return best_banks

# Вверх дном
def reverse_dict(book)->dict:
    reverse_book = {}
    for key,value in book.items():
     reverse_book[value] = key
    return reverse_book

# Структурируем данные
def merge_lists(dates,rates)->dict:
    return dict(zip(dates, rates)) # возвращаем словарь из объединенных при помощи zip списков






