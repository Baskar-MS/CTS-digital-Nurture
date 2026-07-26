# Page Object Model (POM)

Without POM, if the Submit button ID changes from:

submit

to

btn-submit

every Selenium test containing:

driver.find_element(By.ID, "submit")

must be updated individually.

With the Page Object Model, the locator exists in only one file:

SUBMIT_BUTTON = (By.ID, "submit")

Updating it to:

SUBMIT_BUTTON = (By.ID, "btn-submit")

automatically fixes every test using that page object.

This reduces maintenance effort, improves readability, and makes the automation framework scalable.