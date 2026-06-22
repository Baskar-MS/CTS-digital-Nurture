-- Task 1: Subqueries
use college_db;
SELECT s.student_id,
       s.first_name,
       s.last_name
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(enrollment_count)
    FROM
    (
        SELECT COUNT(*) AS enrollment_count
        FROM enrollments
        GROUP BY student_id
    ) avg_enrollments
);

SELECT c.course_name,
       c.course_code
FROM courses c
WHERE NOT EXISTS
(
    SELECT *
    FROM enrollments e
    WHERE e.course_id = c.course_id
    AND e.grade <> 'A'
);

SELECT p.prof_name,
       p.salary,
       p.department_id
FROM professors p
WHERE p.salary =
(
    SELECT MAX(p2.salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
);

SELECT dept_name,
       avg_salary
FROM
(
    SELECT d.dept_name,
           AVG(p.salary) AS avg_salary
    FROM departments d
    JOIN professors p
    ON d.department_id = p.department_id
    GROUP BY d.department_id, d.dept_name
) dept_avg
WHERE avg_salary > 85000;

