from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def find_element(self, *locators):
        return self.driver.find_element(*locators)

    def fill_input(self, value, *locators):
        self.wait.until(EC.visibility_of_element_located(locators))
        self.find_element(*locators).send_keys(value)

    def click_button(self, *locators):
        self.wait.until(EC.element_to_be_clickable(locators))
        self.find_element(*locators).click()

    def is_url_match(self, page_url):
        return self.driver.current_url == page_url