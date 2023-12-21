from src.pages.base_page import BasePage
from ..locators import TaskViewLocators


class TaskViewPage(BasePage):
    def is_task_successfully_added(self, title, description, environment, version, deadline):
        info_box_content = ("Zadanie zostało dodane", "Task successfully added!")

        if (self.get_text(*TaskViewLocators.INFO_BOX) in info_box_content and
                self.get_text(*TaskViewLocators.TITLE).endswith(title) and
                description == self.get_text(*TaskViewLocators.DESCRIPTION) and
                environment == self.get_text(*TaskViewLocators.ENVIRONMENTS) and
                version == self.get_text(*TaskViewLocators.VERSIONS) and
                deadline == self.get_text(*TaskViewLocators.DEADLINE)):
            return True
        else:
            return False