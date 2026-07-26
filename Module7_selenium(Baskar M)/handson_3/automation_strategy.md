# Test Automation Process, Lifecycle & Framework Types
## Digital Nurture 5.0

**Name:** Baskar M

---

# Task 1: Automation Decision and Test Case Selection

## 17. Criteria for Deciding Whether a Test Case Should Be Automated

### 1. Repetitive Execution
Tests that are executed frequently should be automated.

**Application:**
The POST `/api/courses/` endpoint is tested after every code change, making it a good automation candidate.

---

### 2. Stable Functionality
Features that rarely change are ideal for automation.

**Application:**
The API contract for creating a course is stable, so automated tests require minimal updates.

---

### 3. High Business Risk
Critical features should always be automated.

**Application:**
Course creation is a core feature of the Course Management API, so failures have a high business impact.

---

### 4. Data-Driven Testing
Tests requiring multiple input combinations benefit from automation.

**Application:**
The endpoint can be tested with different course names, IDs, departments, and credit values automatically.

---

### 5. Regression Testing
Tests repeated after every release are good automation candidates.

**Application:**
The POST `/api/courses/` endpoint is part of every regression cycle and should be automated.

---

## 18. Automate or Manual?

| Test Case | Decision | Justification |
|-----------|----------|---------------|
| a) Regression test for all CRUD endpoints after every code change | **Automate** | Frequently executed and repetitive. |
| b) Exploratory testing of a new search feature | **Manual** | Requires human observation and creativity. |
| c) Performance test with 100 concurrent users | **Automate** | Performance testing requires automation tools. |
| d) UI test for the login form | **Automate** | Login functionality is stable and executed frequently. |
| e) Verify Swagger API documentation | **Manual** | Documentation changes occasionally and requires review. |
| f) Smoke test after deployment | **Automate** | Quick verification after every deployment. |

---

## 19. Test Automation ROI

### Definition

**Test Automation ROI (Return on Investment)** measures whether the time and cost spent creating automated tests are recovered through repeated execution and reduced manual effort.

### Given

- Automation development time = **4 hours**
- Manual execution time = **30 minutes (0.5 hour)**

### Break-even Calculation

\[
4 \div 0.5 = 8
\]

**Break-even Point = 8 test executions**

After the **10th run**, a **20% maintenance overhead** applies.

Maintenance per run:

20% of 4 hours = **0.8 hour**

Although maintenance slightly increases long-term cost, automation continues to save time because manual execution would still require repeated effort for every regression cycle.

---

## 20. Flaky Tests

### Definition

A **flaky test** is a test that sometimes passes and sometimes fails even though the application has not changed.

### Example

A Selenium login test fails occasionally because the page has not fully loaded before clicking the Login button.

### Prevention Strategies

1. Use **Explicit Waits** instead of fixed delays.
2. Use reliable and unique element locators (ID, Name, CSS Selector).
3. Ensure the test environment and test data remain stable and independent.

---

# Task 2: Compare Automation Framework Types

## 21. Framework Comparison

### 1. Linear Framework

**Description**

The Linear Framework records test steps in sequence without separating test logic or reusable components.

**Advantage**

Easy to learn and implement.

**Disadvantage**

Poor reusability and difficult maintenance.

**Course Management Example**

Automating only the login process for a small demo application.

---

### 2. Modular Framework

**Description**

The application is divided into reusable modules such as Login, Dashboard, and Course Management.

**Advantage**

High code reusability.

**Disadvantage**

Requires careful planning and modular design.

**Course Management Example**

Reuse the Login module across course creation, editing, and enrollment tests.

---

### 3. Data-Driven Framework

**Description**

Test data is stored separately in Excel, CSV, or JSON files while the test script remains unchanged.

**Advantage**

Supports testing multiple datasets using one script.

**Disadvantage**

Managing large datasets can become complex.

**Course Management Example**

Execute login tests using multiple username-password combinations from an Excel file.

---

### 4. Keyword-Driven Framework

**Description**

Tests are created using keywords such as Login, Click, Verify, and Logout instead of programming logic.

**Advantage**

Non-technical testers can contribute.

**Disadvantage**

Initial framework setup is more complex.

**Course Management Example**

Business analysts define test cases using keywords without writing Selenium code.

---

### 5. Hybrid Framework

**Description**

Combines Modular, Data-Driven, and Keyword-Driven approaches to achieve flexibility, maintainability, and scalability.

**Advantage**

Highly reusable, scalable, and suitable for large projects.

**Disadvantage**

More complex to design and maintain initially.

**Course Management Example**

Automate login, course creation, enrollment, and user management using reusable page objects and external test data.

---

## 22. Recommended Framework

### Recommendation

A **Hybrid Framework** combining:

- **Modular Framework**
- **Data-Driven Framework**
- **Keyword-Driven Framework**

### Justification

- Supports testing with **50 different username/password combinations** using external data.
- Allows reuse of login functionality across **20 test cases**.
- Enables both technical and non-technical team members to create and maintain tests.
- Easy to scale as the Course Management application grows.
- Reduces maintenance effort through reusable components.

---

## 23. Hybrid Framework Folder Structure

```text
CourseManagementAutomation/
│
├── config/
│   ├── config.properties
│   └── environment.properties
│
├── testdata/
│   ├── LoginData.xlsx
│   ├── CourseData.xlsx
│   └── Users.csv
│
├── pages/
│   ├── LoginPage.py
│   ├── DashboardPage.py
│   ├── CoursePage.py
│   └── EnrollmentPage.py
│
├── tests/
│   ├── test_login.py
│   ├── test_create_course.py
│   ├── test_update_course.py
│   └── test_enrollment.py
│
├── utilities/
│   ├── BrowserUtils.py
│   ├── WaitUtils.py
│   ├── ExcelReader.py
│   └── Logger.py
│
├── reports/
│
├── screenshots/
│
├── drivers/
│
├── requirements.txt
│
└── README.md
```

### Folder Description

- **config/** – Stores configuration files.
- **testdata/** – Stores Excel, CSV, or JSON test data.
- **pages/** – Contains Page Object Model (POM) classes.
- **tests/** – Contains Selenium test scripts.
- **utilities/** – Common helper methods such as waits, logging, and data reading.
- **reports/** – Automation execution reports.
- **screenshots/** – Captured screenshots for failed tests.
- **drivers/** – Browser drivers such as ChromeDriver.

---

# Conclusion

This hands-on covered the process of selecting suitable test cases for automation, evaluating automation ROI, understanding flaky tests, and comparing the five major automation framework types. Based on the Course Management project requirements, a **Hybrid Framework** is the most suitable choice because it combines modularity, data-driven testing, and keyword-driven capabilities, making the automation suite scalable, reusable, and easy to maintain.