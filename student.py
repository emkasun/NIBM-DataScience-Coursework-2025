class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.courses = []
        self.grades = {}

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} enrolled in {course}")
        else:
            print(f"{self.name} is already enrolled in {course}")

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"{self.name} dropped {course}")
        else:
            print(f"{self.name} is not enrolled in {course}")

    def add_grade(self, course, grade):
        if course in self.courses:
            self.grades[course] = grade
        else:
            print(f"{self.name} is not enrolled in {course}, cannot assign grade.")

    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        return round(sum(self.grades.values()) / len(self.grades), 2)

    def get_academic_status(self):
        gpa = self.calculate_gpa()
        if gpa >= 3.5:
            return "Dean's List"
        elif gpa >= 2.0:
            return "Good Standing"
        else:
            return "Probation"


class UndergraduateStudent(Student):
    def get_responsibilities(self):
        return "Attend lectures, complete assignments, and exams."


class GraduateStudent(Student):
    def get_responsibilities(self):
        return "Conduct research, attend seminars, and publish papers."
from person import Person