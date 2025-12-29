import unittest
from school import (
    get_students,
    get_classes,
    get_links,
    students_with_ov,
    average_grade_by_class,
    classes_with_A_students
)


class TestSchoolQueries(unittest.TestCase):

    def setUp(self):
        self.students = get_students()
        self.classes = get_classes()
        self.links = get_links()

    # ТЕСТ 1
    def test_students_with_ov(self):
        result = students_with_ov(self.students, self.classes)
        expected = {
            ("Иванов", "10А"),
            ("Петров", "10А"),
            ("Сидоров", "11Б"),
            ("Смирнов", "11Б"),
            ("Кузнецов", "9А"),
        }
        self.assertEqual(set(result), expected)



    # ТЕСТ 2
    def test_average_grade_by_class(self):
        result = average_grade_by_class(self.students, self.classes)
        self.assertIn(("11Б", 77.0), result)
        self.assertIn(("9А", 88.0), result)
        self.assertIn(("10А", 88.5), result)
        self.assertIn(("10Б", 95.0), result)

    # ТЕСТ 3
    def test_classes_with_A_students(self):
        result = classes_with_A_students(self.students, self.classes, self.links)

        class_names = [item[0] for item in result]
        self.assertIn("10А", class_names)
        self.assertIn("9А", class_names)


if __name__ == "__main__":
    unittest.main()
