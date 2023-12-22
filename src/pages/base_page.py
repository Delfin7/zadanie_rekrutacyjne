from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def find_element(self, *locators) -> WebElement:
        self.wait.until(EC.visibility_of_element_located(locators))
        return self.driver.find_element(*locators)

    def fill_input(self, value: str, *locators) -> None:
        self.find_element(*locators).send_keys(value)

    def click_button(self, *locators) -> None:
        self.find_element(*locators).click()

    def is_url_match(self, page_url: str) -> bool:
        return self.driver.current_url == page_url

    def get_text(self, *locators) -> str:
        return self.find_element(*locators).text
