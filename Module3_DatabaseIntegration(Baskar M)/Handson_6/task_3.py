"""
Task 87–90 Analysis

Before Optimization:
- Accessing enrollment.student and enrollment.course
  inside a loop causes additional SQL queries.
- This is known as the N+1 Query Problem.

After Optimization:
- joinedload() loads Student and Course data
  together with Enrollment using JOINs.
- All related data is fetched in a single query.

Result:
Before: Multiple SQL Queries (N+1)
After: Single JOIN Query
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from Models import Department, Student, Course, Enrollment

engine = create_engine(
    "mysql+pymysql://root:5907cse%40123@localhost/college_db_orm",
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()

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

print("\n===== ENROLLMENTS WITH JOINEDLOAD =====")

# Task 88: Eager Loading

enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

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

if student:
    student.enrollment_year = 2024
    session.commit()
    print("Updated:", student.first_name)

print("\n===== DELETE =====")

# Task 86: DELETE

enrollment = session.query(Enrollment).first()

if enrollment:
    session.delete(enrollment)
    session.commit()
    print("Enrollment deleted")

session.close()