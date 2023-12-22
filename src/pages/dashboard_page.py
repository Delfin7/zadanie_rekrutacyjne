from src.pages.base_page import BasePage
from ..locators import DashboardPageLocators
from selenium.webdriver.common.keys import Keys


class DashboardPage(BasePage):
    def change_project(self, project_name: str) -> None:
        self.click_button(*DashboardPageLocators.CHANGE_PROJECT_LIST)
        self.fill_input(project_name, *DashboardPageLocators.PROJECT_SELECT)
        self.fill_input(Keys.ENTER, *DashboardPageLocators.PROJECT_SELECT)

    def go_to_tasks(self) -> None:
        self.click_button(*DashboardPageLocators.TASKS_BUTTON)
