from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import Department, Student, Course, Enrollment

engine = create_engine(
    "mysql+pymysql://root:5907cse%40123@localhost/college_db_orm",
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()

# Task 81: INSERT Departments

cs = Department(
    dept_name="Computer Science",
    head_of_dept="Dr. Ramesh Kumar",
    budget=850000
)

ec = Department(
    dept_name="Electronics",
    head_of_dept="Dr. Priya Nair",
    budget=620000
)

me = Department(
    dept_name="Mechanical",
    head_of_dept="Dr. Suresh Iyer",
    budget=540000
)

session.add_all([cs, ec, me])
session.commit()

# Task 81: INSERT Students

s1 = Student(
    first_name="Arjun",
    last_name="Mehta",
    email="arjun@college.edu",
    department=cs,
    enrollment_year=2022
)

s2 = Student(
    first_name="Priya",
    last_name="Suresh",
    email="priya@college.edu",
    department=cs,
    enrollment_year=2022
)

s3 = Student(
    first_name="Rohan",
    last_name="Verma",
    email="rohan@college.edu",
    department=ec,
    enrollment_year=2021
)

s4 = Student(
    first_name="Sneha",
    last_name="Patel",
    email="sneha@college.edu",
    department=me,
    enrollment_year=2023
)

s5 = Student(
    first_name="Vikram",
    last_name="Das",
    email="vikram@college.edu",
    department=cs,
    enrollment_year=2022
)

session.add_all([s1, s2, s3, s4, s5])
session.commit()

# Task 82: INSERT Courses

c1 = Course(
    course_name="Data Structures",
    course_code="CS101",
    credits=4,
    department=cs
)

c2 = Course(
    course_name="Database Systems",
    course_code="CS102",
    credits=3,
    department=cs
)

c3 = Course(
    course_name="Circuit Theory",
    course_code="EC101",
    credits=3,
    department=ec
)

session.add_all([c1, c2, c3])
session.commit()

# Task 82: INSERT Enrollments

e1 = Enrollment(
    student=s1,
    course=c1
)

e2 = Enrollment(
    student=s1,
    course=c2
)

e3 = Enrollment(
    student=s2,
    course=c1
)

e4 = Enrollment(
    student=s3,
    course=c3
)

session.add_all([e1, e2, e3, e4])
session.commit()

print("\n===== STUDENTS IN COMPUTER SCIENCE =====")

# Task 83: READ

students = (
    session.query(Student)
    .join(Department)
    .filter(Department.dept_name == "Computer Science")
    .all()
)

for student in students:
    print(student.first_name, student.last_name)

print("\n===== ENROLLMENTS =====")

# Task 84: READ

enrollments = session.query(Enrollment).all()

for enrollment in enrollments:
    print(
        enrollment.student.first_name,
        "->",
        enrollment.course.course_name
    )

print("\n===== UPDATE =====")

# Task 85: UPDATE

student = (
    session.query(Student)
    .filter(Student.email == "arjun@college.edu")
    .first()
)

student.enrollment_year = 2024

session.commit()

print("Updated:", student.first_name)

print("\n===== DELETE =====")

# Task 86: DELETE

enrollment = session.query(Enrollment).first()

session.delete(enrollment)

session.commit()

print("Enrollment deleted")

session.close()

