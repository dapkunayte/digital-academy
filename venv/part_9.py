from collections import defaultdict

def reverse_number(number) -> list:
    str_number = str(number)
    return list(str_number)[::-1]  # используем срез для разворота списка

def is_palindrome(word) -> bool:
    if not isinstance(
            word, str):  # проверка на тип входных данных (для обработки чисел)
        word = str(word)
    if word[::-1] == word:  # срез для разворота строки и сравнение с оригиналом
        return True
    else:
        return False

def dean_office(students_info, need_to):
    # имена в алфавитном порядке
    if need_to == 'sorted_names':
        names = []
        for student in students_info:
            name = student[0]
            names.append(name)
        return sorted(names)

    # cамый младший и старший
    if need_to == 'sorted_ages':
        ages = {}
        for student in students_info:
            name, age = student[0], student[1]
            ages[name] = age
        sorted_age = sorted(ages.items())
        return sorted_age[0], sorted_age[len(sorted_age) - 1]  # максимум

    # лучший студент
    if need_to == 'best_marks_in_group':
        best_marks_in_group = {}
        for student in students_info:
            name, group, marks = student[0], student[2], student[3]
            if group in best_marks_in_group:
                # best_marks_in_group[group][1] - 1 отвечает за местоположение
                # средней оценки в группе
                if best_marks_in_group[group][1] < sum(marks) / len(marks):
                    best_marks_in_group[group] = [
                        name, sum(marks) / len(marks)]
            else:
                best_marks_in_group[group] = [name, sum(marks) / len(marks)]
        return best_marks_in_group

    # средний балл по всем предметам для каждой группы
    if need_to == 'mean_marks':
        marks_list = defaultdict(list)
        for student in students_info:
            group, marks = student[2], student[3]
            marks_list[group].append(marks)
        group_marks = defaultdict(list)
        for group in marks_list:
            i = 1
            for marks in zip(
                    *marks_list[group]):  # не особо эффективно из-за вложенного цикла, но другого решения не нашёл
                group_marks[group].append(
                    ['Предмет ' + str(i), sum(marks) / len(marks)])
                i += 1
        return dict(group_marks)
