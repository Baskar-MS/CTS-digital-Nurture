# SDLC vs TDLC – V-Model & Agile QA Integration
## Digital Nurture 5.0

**Name:** Baskar M

---

# Task 1: V-Model Mapping

## 9. V-Model Diagram

```text
                 SDLC (Development)

        Requirements
              |
              |
        System Design
              |
              |
      Architecture Design
              |
              |
        Module Design
              |
              |
            Coding
              ▲
              |
      Unit Testing
              |
      Integration Testing
              |
        System Testing
              |
     Acceptance Testing

               TDLC (Testing)
```

### SDLC ↔ TDLC Mapping

| SDLC Phase | Corresponding TDLC Phase |
|------------|--------------------------|
| Requirements | Acceptance Testing |
| System Design | System Testing |
| Architecture Design | Integration Testing |
| Module Design | Unit Testing |
| Coding | Implementation |

---

## 10. Test Artifacts Produced During Development

| SDLC Phase | TDLC Phase | Test Artifact Produced |
|------------|------------|------------------------|
| Requirements | Acceptance Testing | Acceptance Test Plan, User Acceptance Test Cases |
| System Design | System Testing | System Test Plan, System Test Cases |
| Architecture Design | Integration Testing | Integration Test Plan and Integration Test Cases |
| Module Design | Unit Testing | Unit Test Cases and Unit Test Plan |
| Coding | All Testing | Source Code ready for testing |

---

## 11. Entry and Exit Criteria

### Unit Testing

**Entry Criteria**
- Module development completed.
- Source code is available.
- Unit test cases are prepared.

**Exit Criteria**
- All unit test cases executed.
- No critical defects remain.
- Code coverage achieved.

---

### Integration Testing

**Entry Criteria**
- Unit testing completed successfully.
- Modules integrated.
- Integration test cases prepared.

**Exit Criteria**
- All integration test cases executed.
- Interfaces work correctly.
- Critical integration defects fixed.

---

### System Testing

**Entry Criteria**
- Entire application integrated.
- Test environment ready.
- System test cases available.

**Exit Criteria**
- Functional and non-functional tests completed.
- No open Critical or High severity defects.
- Test summary report prepared.

---

### Acceptance Testing (UAT)

**Entry Criteria**
- System testing completed.
- Business requirements finalized.
- UAT environment ready.

**Exit Criteria**
- Customer approves the application.
- Business requirements satisfied.
- Product ready for deployment.

---

## 12. Early QA Engagement in the V-Model

### 1. Requirements Review

QA reviews the Software Requirement Specification (SRS) to identify ambiguous, incomplete, or conflicting requirements before development begins.

**Example**
Verify that the Course Management API clearly specifies mandatory fields such as Course ID, Course Name, Credits, and Department.

---

### 2. Design Review

QA participates in system and architecture design discussions to identify possible testing challenges and prepare test scenarios early.

**Example**
Review API endpoint designs (`POST`, `GET`, `PUT`, `DELETE`) before coding begins to ensure they are testable.

---

# Task 2: Agile QA and Shift-Left Testing

## 13. Problems in Waterfall Testing

### Problem 1
Defects are discovered very late after development, making them expensive to fix.

### Problem 2
Requirement misunderstandings remain unnoticed until testing begins.

### Problem 3
Project delivery is delayed because testing starts only after coding is completed.

---

## 14. QA Role in Agile Ceremonies

### Sprint Planning

- Understand user stories.
- Define acceptance criteria.
- Estimate testing effort.
- Prepare test scenarios.

---

### Daily Standup

- Report testing progress.
- Discuss blocked issues.
- Coordinate with developers on defect fixes.

---

### Sprint Review

- Validate completed features.
- Demonstrate tested functionality.
- Verify acceptance criteria are met.

---

### Sprint Retrospective

- Discuss testing challenges.
- Suggest process improvements.
- Recommend automation opportunities.

---

## 15. Shift-Left Testing Practices

### a) Review Requirements for Testability

QA reviews requirements before development starts to ensure they are complete, clear, and testable.

**Course Management API Example**
Confirm that every API endpoint has defined request and response formats.

---

### b) Write Test Cases Before Coding (TDD/BDD)

Test cases are prepared before developers begin implementation.

**Course Management API Example**
Prepare test cases for `POST /api/courses/` before writing the API code.

---

### c) Static Code Analysis

Analyze source code using automated tools without executing the application.

**Course Management API Example**
Use tools like SonarQube or pylint to identify coding issues and security vulnerabilities.

---

### d) API Contract Testing

Verify API request and response formats before integrating with other services.

**Course Management API Example**
Ensure `/api/courses/` always returns the expected JSON structure defined in the API specification.

---

## 16. Acceptance Criteria (Given-When-Then)

### Scenario 1 – Happy Path

**Given**
The college admin is logged in.

**When**
The admin enters valid course details and submits the form.

**Then**
The course is successfully created and a confirmation message is displayed.

---

### Scenario 2 – Duplicate Course Code

**Given**
A course with the same course code already exists.

**When**
The admin submits another course using the same course code.

**Then**
The system displays an error message indicating that the course code already exists and the course is not created.

---

### Scenario 3 – Missing Required Fields

**Given**
The admin opens the Create Course page.

**When**
The admin submits the form without entering mandatory fields such as Course Name or Course Code.

**Then**
The system displays validation messages and prevents the course from being created.

---

# Conclusion

This hands-on explained the relationship between SDLC and TDLC using the V-Model, including phase mappings, test artifacts, entry and exit criteria, and early QA involvement. It also covered Agile QA practices, the Shift-Left testing approach, and acceptance criteria written in Given-When-Then format. These concepts help improve software quality by identifying defects early and ensuring collaboration between developers and QA engineers throughout the software development lifecycle.