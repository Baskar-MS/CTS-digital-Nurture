# Task 3: Identify and Fix the N+1 Problem

import mysql.connector
import time

conn = mysql.connector.connect(
host="localhost",
user="root",
password="5907cse@123",
database="college_db"
)

cursor = conn.cursor(dictionary=True)

print("========== N+1 QUERY VERSION ==========")

start_time = time.time()

query_count = 1

cursor.execute("SELECT * FROM enrollments")
enrollments = cursor.fetchall()

for enrollment in enrollments:
    cursor.execute(
        "SELECT first_name, last_name FROM students WHERE student_id = %s",
        (enrollment['student_id'],)
    )

    student = cursor.fetchone()

    print(
        f"Enrollment ID: {enrollment['enrollment_id']} | "
        f"Student: {student['first_name']} {student['last_name']}"
    )

    query_count += 1


end_time = time.time()

print("\nQueries Executed:", query_count)
print("Execution Time:", round(end_time - start_time, 6), "seconds")

print("\n========== OPTIMIZED JOIN VERSION ==========")

start_time = time.time()

query_count = 1

cursor.execute("""
SELECT e.enrollment_id,
s.first_name,
s.last_name
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
""")

results = cursor.fetchall()

for row in results:
    print(
        f"Enrollment ID: {row['enrollment_id']} | "
        f"Student: {row['first_name']} {row['last_name']}"
    )

end_time = time.time()

print("\nQueries Executed:", query_count)
print("Execution Time:", round(end_time - start_time, 6), "seconds")

cursor.close()
conn.close()

print("\n========== ANALYSIS ==========")
print("N+1 Version Queries = 13")
print("JOIN Version Queries = 1")
print("For 10,000 enrollments:")
print("N+1 Version = 10,001 queries")
print("JOIN Version = 1 query")
"""
               OUTPUT
========== N+1 QUERY VERSION ==========
Enrollment ID: 1 | Student: Arjun Mehta
Enrollment ID: 2 | Student: Arjun Mehta
Enrollment ID: 3 | Student: Priya Suresh
Enrollment ID: 4 | Student: Priya Suresh
Enrollment ID: 5 | Student: Rohan Verma
Enrollment ID: 7 | Student: Vikram Das
Enrollment ID: 8 | Student: Vikram Das
Enrollment ID: 9 | Student: Kavya Menon
Enrollment ID: 11 | Student: Deepika Rao
Enrollment ID: 12 | Student: Deepika Rao
Enrollment ID: 13 | Student: Arjun Mehta
Enrollment ID: 14 | Student: Kavya Menon
Enrollment ID: 15 | Student: Rohan Verma
Enrollment ID: 16 | Student: Sneha Patel
Enrollment ID: 19 | Student: Aditya Singh
Enrollment ID: 20 | Student: Baskar M

Queries Executed: 17
Execution Time: 0.006004 seconds

========== OPTIMIZED JOIN VERSION ==========
Enrollment ID: 1 | Student: Arjun Mehta
Enrollment ID: 2 | Student: Arjun Mehta
Enrollment ID: 13 | Student: Arjun Mehta
Enrollment ID: 3 | Student: Priya Suresh
Enrollment ID: 4 | Student: Priya Suresh
Enrollment ID: 15 | Student: Rohan Verma
Enrollment ID: 5 | Student: Rohan Verma
Enrollment ID: 16 | Student: Sneha Patel
Enrollment ID: 7 | Student: Vikram Das
Enrollment ID: 8 | Student: Vikram Das
Enrollment ID: 14 | Student: Kavya Menon
Enrollment ID: 9 | Student: Kavya Menon
Enrollment ID: 19 | Student: Aditya Singh
Enrollment ID: 11 | Student: Deepika Rao
Enrollment ID: 12 | Student: Deepika Rao
Enrollment ID: 20 | Student: Baskar M

Queries Executed: 1
Execution Time: 0.001318 seconds

========== ANALYSIS ==========
N+1 Version Queries = 13
JOIN Version Queries = 1
For 10,000 enrollments:
N+1 Version = 10,001 queries
JOIN Version = 1 query
"""