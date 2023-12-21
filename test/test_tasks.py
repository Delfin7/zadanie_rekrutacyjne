from test.base_test import BaseTest
from src.pages import login_page, dashboard_page, tasks_page, add_task_page, task_view_page


class Tasks(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = login_page.LoginPage(self.driver)
        self.dashboard_page = dashboard_page.DashboardPage(self.driver)
        self.tasks_page = tasks_page.TasksPage(self.driver)
        self.add_task_page = add_task_page.AddTask(self.driver)
        self.task_view_page = task_view_page.TaskViewPage(self.driver)

    def test_add_task_positive(self):
        project_name = "zadanie_Kamil"
        title = "title"
        description = "desc"
        environment = "TEST"
        version = "TEST"
        deadline = "2023-12-04 23:59:00"

        self.login_page.login(self.CORRECT_EMAIL, self.CORRECT_PASSWORD)
        self.dashboard_page.change_project(project_name)
        self.dashboard_page.go_to_tasks()
        self.tasks_page.go_to_add_task()
        self.add_task_page.add_task(title, description, environment, version, deadline)

        self.assertTrue(self.task_view_page.is_task_successfully_added(
            title, description, environment, version, deadline))
