from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckboxPage(BasePage):

    FIRST_CHECKBOX = (By.ID, "isAgeSelected")

    def check_option(self, index=1):
        checkbox = self.driver.find_element(*self.FIRST_CHECKBOX)
        if not checkbox.is_selected():
            checkbox.click()

    def uncheck_option(self, index=1):
        checkbox = self.driver.find_element(*self.FIRST_CHECKBOX)
        if checkbox.is_selected():
            checkbox.click()

    def is_option_checked(self, index=1):
        return self.driver.find_element(*self.FIRST_CHECKBOX).is_selected()