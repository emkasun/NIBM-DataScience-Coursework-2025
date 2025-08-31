from person import Staff
from student import UndergraduateStudent, GraduateStudent
from faculty import Professor, Lecturer, TeachingAssistant
from department import Course, Department

# Create Department
cs_dept = Department("Computer Science")

# Add Courses
algo = Course("CS101", "Algorithms", 3)
ml = Course("CS201", "Machine Learning", 3, prerequisites=["Algorithms"])
cs_dept.add_course(algo)
cs_dept.add_course(ml)

# Faculty
prof = Professor("Dr. Smith", 50, "smith@uni.edu", "F001")
lecturer = Lecturer("Dr. John", 40, "john@uni.edu", "F002")
ta = TeachingAssistant("Alice", 28, "alice@uni.edu", "F003")
cs_dept.assign_faculty(prof)
cs_dept.assign_faculty(lecturer)
cs_dept.assign_faculty(ta)

# Students
ug_student = UndergraduateStudent("Bob", 20, "bob@student.uni.edu", "S001")
grad_student = GraduateStudent("Eve", 24, "eve@student.uni.edu", "S002")

# Enroll students
algo.enroll_student(ug_student)
ug_student.add_grade("Algorithms", 3.8)
print(ug_student.name, "GPA:", ug_student.calculate_gpa(), "-", ug_student.get_academic_status())

ml.enroll_student(grad_student)  # should fail (no prereq yet)
algo.enroll_student(grad_student)
grad_student.add_grade("Algorithms", 3.2)
ml.enroll_student(grad_student)  # now should work

# Faculty responsibilities
for f in [prof, lecturer, ta]:
    print(f"{f.name} responsibilities: {f.get_responsibilities()} - {f.calculate_workload()}")
