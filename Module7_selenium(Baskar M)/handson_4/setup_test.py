"""
Digital Nurture 5.0
Hands-On 4
QA Concepts & Selenium Basics

Task 24:
Selenium Architecture

1. WebDriver
- WebDriver is the core component of Selenium.
- It communicates directly with browser drivers (ChromeDriver, GeckoDriver, etc.)
  using the WebDriver protocol.
- It allows Python code to control browser actions such as opening pages,
  clicking buttons, entering text, and reading page information.

2. Selenium Grid
- Selenium Grid allows tests to run on multiple machines, operating systems,
  and browsers simultaneously.
- It helps reduce execution time by running tests in parallel.

3. Selenium IDE
- Selenium IDE is a browser extension used for recording and replaying user actions.
- It is useful for beginners and can generate automation scripts in different
  programming languages.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Task 27: Headless Mode
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Task 26
# Implicit Wait
driver.implicitly_wait(10)

# Implicit waits apply globally to every element lookup.
# They may slow execution and make debugging difficult.
# Explicit waits are preferred because they wait only for specific conditions.

driver.get("https://www.lambdatest.com/selenium-playground/")

print("Page Title:")
print(driver.title)

driver.quit()