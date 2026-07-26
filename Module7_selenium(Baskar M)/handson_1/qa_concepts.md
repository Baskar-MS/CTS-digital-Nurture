# QA Concepts & Selenium Basics – Hands-On 1
## Digital Nurture 5.0

**Name:** Baskar M

---

# Task 1: Map Testing Types to a Real System

## 1. Testing Types with Examples

### Unit Testing
**Description:**
Tests a single function or method independently.

**Example Test Case:**
Test the `create_course()` function to verify that it correctly creates a course object when valid course details are provided.

**Type:** Functional Testing

---

### Integration Testing
**Description:**
Tests interaction between two or more components.

**Example Test Case:**
Send a POST request to `/api/courses/` and verify that the course is successfully stored in the database.

**Type:** Functional Testing

---

### System Testing
**Description:**
Tests the complete application from beginning to end.

**Example Test Case:**
Create a new course using the API and retrieve it using GET `/api/courses/` to ensure the complete workflow functions correctly.

**Type:** Functional Testing

---

### User Acceptance Testing (UAT)
**Description:**
Validates that the application satisfies business requirements.

**Example Test Case:**
A college administrator logs in, creates a new course, edits course details, and confirms the changes are visible in the course list.

**Type:** Functional Testing

---

## 2. Functional vs Non-Functional Testing

### Functional Testing
Checks whether the system performs the required functions correctly.

**Example**
Verify that POST `/api/courses/` successfully creates a course when valid data is provided.

---

### Non-Functional Testing
Checks how well the system performs.

**Example**
Performance Testing:
Verify that the Course Management API responds within **2 seconds** when handling **100 concurrent users**.

---

## 3. Black-Box Testing vs White-Box Testing

| Black-Box Testing | White-Box Testing |
|-------------------|------------------|
| Tests functionality without knowing the internal code. | Tests internal code structure and logic. |
| Focuses on inputs and outputs. | Focuses on code paths, conditions, and branches. |
| Usually performed by QA Testers. | Usually performed by Developers. |
| No programming knowledge required. | Programming knowledge is required. |

**QA Tester:** Mainly performs **Black-Box Testing**

**Developer:** Mainly performs **White-Box Testing**

---

## 4. Formal Test Cases for POST /api/courses/

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|--------------|-------------|---------------|------------|-----------------|---------------|-----------|
| TC001 | Create a course with valid data | API server is running | 1. Send POST request with valid course details | HTTP 201 Created and course stored successfully | | |
| TC002 | Create a course with missing course name | API server is running | 1. Send POST request without course name | HTTP 400 Bad Request with validation error | | |
| TC003 | Create duplicate course | Course already exists | 1. Send POST request using existing course details | Error message indicating duplicate course or conflict | | |

---

# Task 2: Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

```
New
 ↓
Assigned
 ↓
Open
 ↓
Fixed
 ↓
Retest
 ↓
Verified
 ↓
Closed
```

### Rejected
If the reported issue is not a valid defect or cannot be reproduced, it is marked as **Rejected**.

### Deferred
If the defect is valid but fixing it is postponed to a future release due to low priority or time constraints, it is marked as **Deferred**.

---

## 6. Severity and Priority Classification

### a) POST /api/courses/ returns 500 Internal Server Error for all requests

**Severity:** Critical

**Priority:** P1

**Justification:**
The API is completely unusable because no course can be created.

---

### b) Course names longer than 150 characters are silently truncated

**Severity:** Medium

**Priority:** P3

**Justification:**
The system continues working but data integrity is affected.

---

### c) Swagger documentation contains a typo

**Severity:** Low

**Priority:** P4

**Justification:**
Only documentation is affected; application functionality remains unchanged.

---

### d) Login occasionally returns 401 on the first attempt

**Severity:** High

**Priority:** P1

**Justification:**
Although intermittent, login failures affect users significantly and require immediate investigation.

---

## 7. Defect Report

**Defect ID:** DEF-001

**Title:**
POST /api/courses/ returns 500 Internal Server Error

**Environment:**
Windows 11, Python 3.x, Django REST Framework, Chrome Browser

**Build Version:**
v1.0

**Severity:**
Critical

**Priority:**
P1

**Steps to Reproduce:**

1. Start the Course Management API.
2. Open Postman.
3. Send POST request to `/api/courses/`.
4. Enter valid course details.
5. Click Send.

**Expected Result:**

The API should create a new course and return HTTP 201 Created.

**Actual Result:**

The API returns HTTP 500 Internal Server Error.

**Attachments:**

Screenshot of 500 Internal Server Error.

---

## 8. Difference Between Severity and Priority

### Severity
Severity indicates **how serious the defect impacts the application**.

### Priority
Priority indicates **how urgently the defect should be fixed**.

### Example

Suppose the company logo is missing from the CEO's dashboard before a product demonstration.

- Severity: Low (the application still works)
- Priority: High (must be fixed immediately because the CEO will present it)

This example shows that **High Priority does not always mean High Severity.**

---

# Conclusion

This hands-on covered the basic concepts of Quality Assurance, including testing levels, functional and non-functional testing, black-box and white-box testing, defect lifecycle, severity vs priority, defect reporting, and formal test case writing. These concepts form the foundation for software testing and future automation testing using Selenium.