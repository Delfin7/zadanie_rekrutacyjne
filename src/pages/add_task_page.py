from src.pages.base_page import BasePage
from ..locators import AddTaskPageLocators


class AddTask(BasePage):
    def add_task(self, tittle, description, environment, version, deadline):
        self.fill_input(tittle, *AddTaskPageLocators.TITLE_INPUT)
        self.fill_input(description, *AddTaskPageLocators.DESCRIPTION_INPUT)
        self.fill_input(environment, *AddTaskPageLocators.ENVIRONMENTS_INPUT)
        self.click_button(*AddTaskPageLocators.ENVIRONMENTS_LIST)
        self.fill_input(version, *AddTaskPageLocators.VERSIONS_INPUT)
        self.click_button(*AddTaskPageLocators.VERSIONS_LIST)
        self.fill_input(deadline, *AddTaskPageLocators.DEADLINE_INPUT)
        self.click_button(*AddTaskPageLocators.ASSIGN_TO_ME_BUTTON)
        self.click_button(*AddTaskPageLocators.SAVE_BUTTON)
