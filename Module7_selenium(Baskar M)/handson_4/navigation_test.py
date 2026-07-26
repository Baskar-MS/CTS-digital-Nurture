from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()
driver.implicitly_wait(10)

# Open Selenium Playground
driver.get("https://www.lambdatest.com/selenium-playground/")

# Click "Simple Form Demo"
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

# Verify URL
assert "simple-form-demo" in driver.current_url

print("Current URL:")
print(driver.current_url)

# Navigate Back
driver.back()

# Open Google in New Tab
driver.execute_script('window.open("https://www.google.com");')

# List all tabs
print("\nWindow Handles:")
print(driver.window_handles)

# Switch to Google Tab
driver.switch_to.window(driver.window_handles[1])

print("\nGoogle Title:")
print(driver.title)

# Switch Back
driver.switch_to.window(driver.window_handles[0])

# Take Screenshot
driver.save_screenshot("playground_screenshot.png")

if os.path.exists("playground_screenshot.png"):
    print("\nScreenshot Saved Successfully")
else:
    print("\nScreenshot Failed")

# Window Size
print("\nCurrent Window Size:")
print(driver.get_window_size())

driver.set_window_size(1280, 800)

print("\nNew Window Size:")
print(driver.get_window_size())

# Consistent window size ensures the UI renders the same way
# during every test execution, making responsive UI tests reliable.

driver.quit()