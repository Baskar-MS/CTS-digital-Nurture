CREATE DATABASE college_db_orm;
USE college_db_orm;

SHOW TABLES;
USE college_db_orm;

SELECT * FROM departments;
SELECT * FROM students;
SELECT * FROM courses;
SELECT * FROM enrollments;

USE college_db_orm;

SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE enrollments;
TRUNCATE TABLE courses;
TRUNCATE TABLE students;
TRUNCATE TABLE departments;

SET FOREIGN_KEY_CHECKS = 1;