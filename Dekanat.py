class Student:
    students = []

    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.scores = {}
        Student.students.append(self)

    def add_score(self, subject, score):
        if subject not in self.scores.keys():
            self.scores[subject] = score

    def get_average_score(self):
        scores_values = self.scores.values()
        result = sum(scores_values) / len(scores_values)
        return result

    @staticmethod
    def return_students():
        return Student.students


class Group:
    def __init__(self, group_name):
        self.group_name = group_name

    def get_average_score_by_group(self, students):
        groups_score = []
        for student in students:
            if self == student.group:
                groups_score.append(student.get_average_score())
        result = sum(groups_score) / len(groups_score)
        print(f"Average {self.group_name}'s score is {result}")


class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name

    def get_average_score_by_subject(self, students):
        subject_score = []
        for student in students:
            if student.scores[self]:
                subject_score.append(student.scores[self])
        result = sum(subject_score) / len(subject_score)
        print(f"Average {self.subject_name}'s score is {result}")


def get_average_score_by_subject_in_group(subject, group, students):
    score = []
    for student in students:
        if student.group == group:
            if student.scores[subject]:
                score.append(student.get_average_score())
    result = sum(score)/len(score)
    print(f"Average {subject.subject_name}'s score in {group.group_name} is {result}")


# инициализируем студентов
student_1 = Student(name="Dima", group=None)
student_2 = Student(name="Petr", group=None)
student_3 = Student(name="Vasya", group=None)

# инициализируем группы
group_1 = Group("748")
group_2 = Group("749")

# присвоим студентам группы
student_1.group = group_1
student_2.group = group_1
student_3.group = group_2

# инициализируем предметы
subject_1 = Subject("Math")
subject_2 = Subject("Russian")

student_1.add_score(subject_1, 4)
student_1.add_score(subject_2, 4)
student_2.add_score(subject_1, 5)
student_2.add_score(subject_2, 5)
student_3.add_score(subject_1, 3)
student_3.add_score(subject_2, 4)

# получаем средний балл студента
print(f"Average {student_1.name}'s score is {student_1.get_average_score()}")
print(f"Average {student_2.name}'s score is {student_2.get_average_score()}")
print(f"Average {student_3.name}'s score is {student_3.get_average_score()}")

# получить среднее по группе
group_1.get_average_score_by_group(Student.students)
group_2.get_average_score_by_group(Student.students)

# получить среднее по предмету
subject_1.get_average_score_by_subject(Student.students)
subject_2.get_average_score_by_subject(Student.students)


# получить средний балл по предмету в группе
get_average_score_by_subject_in_group(subject_2, group_1, Student.students)
get_average_score_by_subject_in_group(subject_1, group_1, Student.students)
