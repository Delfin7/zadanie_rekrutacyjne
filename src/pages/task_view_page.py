from src.pages.base_page import BasePage
from ..locators import TaskViewLocators
from utilities.task import Task


class TaskViewPage(BasePage):
    def is_task_successfully_added(self, task: Task) -> bool:
        info_box_content = ("Zadanie zostało dodane", "Task successfully added!")

        return (self.get_text(*TaskViewLocators.INFO_BOX) in info_box_content and
                self.get_text(*TaskViewLocators.TITLE).endswith(task.title) and
                task.description == self.get_text(*TaskViewLocators.DESCRIPTION) and
                task.environment == self.get_text(*TaskViewLocators.ENVIRONMENTS) and
                task.version == self.get_text(*TaskViewLocators.VERSIONS) and
                task.deadline == self.get_text(*TaskViewLocators.DEADLINE))
