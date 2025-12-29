class SchoolClass:
    def __init__(self, class_id, name):
        self.class_id = class_id
        self.name = name


class Student:
    def __init__(self, student_id, last_name, grade, class_id):
        self.student_id = student_id
        self.last_name = last_name
        self.grade = grade
        self.class_id = class_id


class StudentInClass:
    def __init__(self, student_id, class_id):
        self.student_id = student_id
        self.class_id = class_id


# ===== ДАННЫЕ =====

def get_classes():
    return [
        SchoolClass(1, "10А"),
        SchoolClass(2, "11Б"),
        SchoolClass(3, "9А"),
        SchoolClass(4, "10Б"),
    ]


def get_students():
    return [
        Student(1, "Иванов", 85, 1),
        Student(2, "Петров", 92, 1),
        Student(3, "Сидоров", 78, 2),
        Student(4, "Кузнецов", 88, 3),
        Student(5, "Алексеев", 95, 4),
        Student(6, "Смирнов", 76, 2),
    ]


def get_links():
    return [
        StudentInClass(1, 1),
        StudentInClass(2, 1),
        StudentInClass(3, 2),
        StudentInClass(4, 3),
        StudentInClass(5, 4),
        StudentInClass(6, 2),
        StudentInClass(1, 2),
        StudentInClass(4, 1),
    ]


# ===== ЛОГИКА (ЗАПРОСЫ) =====

def students_with_ov(students, classes):
    result = []

    for student in students:
        if student.last_name.endswith("ов"):
            class_name = next(
                c.name for c in classes if c.class_id == student.class_id
            )
            result.append((student.last_name, class_name))

    return result



def average_grade_by_class(students, classes):
    grades = {}

    for student in students:
        grades.setdefault(student.class_id, []).append(student.grade)

    result = []
    for class_id, values in grades.items():
        class_name = next(c.name for c in classes if c.class_id == class_id)
        avg = round(sum(values) / len(values), 1)
        result.append((class_name, avg))

    return sorted(result, key=lambda x: x[1])


def classes_with_A_students(students, classes, links):
    result = []

    for school_class in classes:
        if school_class.name.endswith("А"):
            student_ids = {
                link.student_id
                for link in links
                if link.class_id == school_class.class_id
            }

            class_students = [
                student for student in students
                if student.student_id in student_ids
            ]

            result.append((school_class.name, class_students))

    return result
