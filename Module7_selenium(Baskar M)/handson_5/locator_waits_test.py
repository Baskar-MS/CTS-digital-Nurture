"""
Digital Nurture 5.0
Hands-On 5
Locators & Explicit Waits

Target Website:
https://www.lambdatest.com/selenium-playground/
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()
driver.implicitly_wait(10)

wait = WebDriverWait(driver, 10)

##############################################################
# TASK 32
# All Locator Strategies
##############################################################

driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

print("\nTask 32")

# By.ID
element = driver.find_element(By.ID, "user-message")
print("ID Locator ✓")

# By.NAME
element = driver.find_element(By.NAME, "message")
print("NAME Locator ✓")

# By.CLASS_NAME
element = driver.find_element(By.CLASS_NAME, "form-control")
print("CLASS_NAME Locator ✓")

# By.TAG_NAME
element = driver.find_element(By.TAG_NAME, "input")
print("TAG_NAME Locator ✓")

# Absolute XPath
element = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/section[2]/div/div/div[1]/div/div[2]/form/div/input"
)
print("Absolute XPath ✓")

# Relative XPath
element = driver.find_element(
    By.XPATH,
    "//input[@id='user-message']"
)
print("Relative XPath ✓")

##############################################################
# TASK 33
# CSS Selectors
##############################################################

print("\nTask 33")

# CSS using ID
driver.find_element(By.CSS_SELECTOR, "#user-message")
print("CSS ID ✓")

# CSS using attribute
driver.find_element(By.CSS_SELECTOR, "input[name='message']")
print("CSS Attribute ✓")

# CSS Parent > Child
driver.find_element(By.CSS_SELECTOR, "form > div > input")
print("CSS Parent-Child ✓")

##############################################################
# TASK 34
# XPath text() and contains()
##############################################################

driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")

print("\nTask 34")

label = driver.find_element(
    By.XPATH,
    "//label[text()='Option 1']"
)

print(label.text)

labels = driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)

print("Total Option Labels:", len(labels))

##############################################################
# TASK 35
##############################################################

"""
Locator Ranking (Best → Worst)

1. ID
2. NAME
3. CSS Selector
4. Relative XPath
5. CLASS_NAME
6. TAG_NAME
7. Absolute XPath

Reason:

ID
- Fastest
- Unique
- Easy to maintain

NAME
- Usually unique

CSS Selector
- Fast
- Readable
- Preferred over XPath

Relative XPath
- Flexible
- Handles dynamic elements

CLASS_NAME
- Often shared by multiple elements

TAG_NAME
- Usually returns many elements

Absolute XPath
- Breaks whenever page layout changes.
"""

##############################################################
# TASK 36
# Explicit Wait
##############################################################

driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

print("\nTask 36")

success_button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "autoclosable-btn-success")
    )
)

success_button.click()

alert = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")
    )
)

assert "successfully" in alert.text.lower()

print("Alert Text:")
print(alert.text)

##############################################################
# TASK 37
# sleep() vs Explicit Wait
##############################################################

print("\nTask 37")

driver.refresh()

start = time.time()

driver.find_element(By.ID, "autoclosable-btn-success").click()

time.sleep(3)

print("sleep() Time:", round(time.time() - start, 2), "seconds")

driver.refresh()

start = time.time()

driver.find_element(By.ID, "autoclosable-btn-success").click()

wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")
    )
)

print("Explicit Wait Time:", round(time.time() - start, 2), "seconds")

"""
Explicit Wait is preferred because:

- waits only as long as needed
- faster on fast systems
- more reliable on slow systems
- avoids unnecessary delays
"""

##############################################################
# TASK 38
##############################################################

driver.refresh()

button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "autoclosable-btn-success")
    )
)

button.click()

"""
visibility_of_element_located()

Element is present and visible.

element_to_be_clickable()

Element is:
1. Visible
2. Enabled
3. Ready to receive clicks
"""

##############################################################
# TASK 39
# Fluent Wait
##############################################################

driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

print("\nTask 39")

fluent_wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException]
)

row = fluent_wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "tbody tr")
    )
)

print("First Row:")
print(row.text)

driver.quit()