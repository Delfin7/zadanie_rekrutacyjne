from test.base_test import BaseTest
from src.pages import login_page, dashboard_page, tasks_page


class AddTask(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = login_page.LoginPage(self.driver)
        self.dashboard_page = dashboard_page.DashboardPage(self.driver)
        self.tasks_page = tasks_page.TasksPage(self.driver)

    def test_add_task_positive(self):
        project_id = 6043

        self.login_page.login(self.CORRECT_EMAIL, self.CORRECT_PASSWORD)
        self.dashboard_page.change_project(project_id)
        self.dashboard_page.go_to_tasks()
        self.tasks_page.add_task()
        


