import part_9

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Список из числа
    number = 123
    print(part_9.reverse_number(number))

    # Палиндром
    string_false = 'hi'
    string_true = 404
    print(part_9.is_palindrome(string_false))
    print(part_9.is_palindrome(string_true))

    #Деканат
    students_info = [['Кривошеин Илья Андреевич', 2000, '759-B', [5, 3, 4, 3, 3]],
                     ['Петров Илья Андреевич', 2001, '759-С', [5, 3, 4, 4, 4]],
                     ['Смирнов Илья Андреевич', 2002, '759-B', [5, 3, 4, 3, 4]],
                     ['Дметров Илья Андреевич', 2000, '759-С', [5, 5, 4, 4, 4]]]
    sorted_names = 'sorted_names'
    sorted_ages = 'sorted_ages'
    best_marks_in_group = 'best_marks_in_group'
    mean_marks = 'mean_marks'
    print("Имена студентов в алфавитном порядке:", part_9.dean_office(students_info, sorted_names))
    younger_student, older_student = part_9.dean_office(students_info, sorted_ages)
    print("Самый младший студент:", younger_student, "Самый старший студент:", older_student)
    print("Лучшая успеваемость по группам", part_9.dean_office(students_info, best_marks_in_group))
    print("Средний балл по каждой группе по каждому предмету", part_9.dean_office(students_info, mean_marks))

