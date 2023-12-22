from src.pages.base_page import BasePage
from utilities.task import Task
from ..locators import AddTaskPageLocators


class AddTask(BasePage):
    def add_task(self, task: Task) -> None:
        self.fill_input(task.title, *AddTaskPageLocators.TITLE_INPUT)
        self.fill_input(task.description, *AddTaskPageLocators.DESCRIPTION_INPUT)
        self.fill_input(task.environment, *AddTaskPageLocators.ENVIRONMENTS_INPUT)
        self.click_button(*AddTaskPageLocators.ENVIRONMENTS_LIST)
        self.fill_input(task.version, *AddTaskPageLocators.VERSIONS_INPUT)
        self.click_button(*AddTaskPageLocators.VERSIONS_LIST)
        self.fill_input(task.deadline, *AddTaskPageLocators.DEADLINE_INPUT)
        self.click_button(*AddTaskPageLocators.ASSIGN_TO_ME_BUTTON)
        self.click_button(*AddTaskPageLocators.SAVE_BUTTON)
