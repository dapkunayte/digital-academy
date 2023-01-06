def celsius_to_fahrenheit(temp: list) -> list:  # Градусник
    return [(9 / 5) * celsius_temp + 32 for celsius_temp in temp]


print(celsius_to_fahrenheit([39.2, 36.5, 37.3, 37.8]))


def str_len(strings: list) -> list:  # Длинномер
    return [len(string) for string in strings]


print(str_len(['Tina', 'Raj', 'Tom']))


def pow_x_y(x_list: list, y_list: list) -> list:  # Возведение в степень
    return [x ** y for x, y in zip(x_list, y_list)]


print(pow_x_y([2, 3, 4], [10, 11, 12]))


def refactor(sentences: list) -> int:  # Рефакторинг
    return len([1 for sentence in sentences if 'капитан' in sentence])


test_sentences = ['капитан джек воробей',
                  'капитан дальнего плавания',
                  'ваша лодка готова, капитан']
print(refactor(test_sentences))


def lazy_func(n: int) -> list:  # Ленивая функция
    for i in range(n):
        if i == 0:
            yield -10
        elif i % 3 != 0:
            yield 45
        elif i % 5 != 0:
            yield (i / 5) + 93
        else:
            yield i/2


sequence = lazy_func(3)

print(list(lazy_func(3)))
print(list(lazy_func(8)))

print(next(sequence))
print(next(sequence))
print(next(sequence))


def largest_histogram(histogram: list) -> int:  # Самый большой прямоугольник
    len_hist = len(histogram) + 1
    result = [min(histogram[j:j + i])*len(histogram[j:j + i]) for i in range(1, len_hist) for j in range(len_hist - i)]
    return max(result)


print(largest_histogram([2, 1, 4, 5, 1, 3, 3]))



