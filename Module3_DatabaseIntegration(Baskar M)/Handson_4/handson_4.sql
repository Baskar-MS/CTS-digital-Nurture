use college_db;
-- Task 1: Baseline Performance — No Indexes

EXPLAIN
SELECT s.first_name,
       s.last_name,
       c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

/*
EXPLAIN Analysis

Table: students (alias s)
Access Type: ALL
Key Used: NULL
Rows Examined: 10
Extra: Using where

Table: enrollments (alias e)
Access Type: ref
Key Used: student_id
Rows Examined: 2
Extra: Using where

Table: courses (alias c)
Access Type: eq_ref
Key Used: PRIMARY
Rows Examined: 1

Observations:
1. The students table performs a Full Table Scan
   because no index exists on enrollment_year.
2. MySQL examines approximately 10 rows in students.
3. enrollments uses the student_id index.
4. courses uses its PRIMARY KEY.
5. Query cost is low because the dataset is small,
   but performance may degrade as the table grows.
*/
 --Yes. A Full Table Scan occurs on the students table (type = ALL).
 --Rows examined:

--students = 10
--enrollments = 2
--courses = 1
--Query cost from EXPLAIN FORMAT=JSON = 2.87

-- Task 2: Add Indexes and Compare Plans

CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);

CREATE UNIQUE INDEX idx_enrollments_student_course
ON enrollments(student_id, course_id);

CREATE INDEX idx_courses_course_code
ON courses(course_code);

EXPLAIN
SELECT s.first_name,
       s.last_name,
       c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

/*
Comparison with Baseline:

Before Index:
- students table used Access Type = ALL
- Full Table Scan occurred on students
- Rows examined = 10

After Index:
- students table should use the index
  idx_students_enrollment_year
- Access Type may change from ALL to ref/range
- Fewer rows are examined
- Query performance improves

The composite UNIQUE index on
(student_id, course_id)
prevents duplicate enrollments.

The index on course_code improves
search performance for queries filtering
by course code.
*/

