from src.pages.base_page import BasePage
from ..locators import TasksPageLocators


class TasksPage(BasePage):
    def go_to_add_task(self):
        self.click_button(*TasksPageLocators.ADD_A_TASK_BUTTON)
