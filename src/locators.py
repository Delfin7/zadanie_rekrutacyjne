from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login")
    INCORRECT_LOGIN_DATA_ERROR = (By.CSS_SELECTOR, ".login_form_error")


class DashboardPageLocators:
    PROJECT_BUTTON = (By.CSS_SELECTOR, "a[href='http://demo.testarena.pl/kiss/project_view']")


class TasksPageLocators:
    ADD_A_TASK_BUTTON = (By.CSS_SELECTOR, ".button_link")


class AddTaskPageLocators:
    TITLE_INPUT = (By.CSS_SELECTOR, "#title")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "#description")
    ENVIRONMENTS_INPUT = (By.CSS_SELECTOR, "#token-input-environments")
    VERSIONS_INPUT = (By.CSS_SELECTOR, "#token-input-versions")
    PRIORITY_SELECT = (By.CSS_SELECTOR, "#priority")
    DEADLINE_INPUT = (By.CSS_SELECTOR, "#dueDate")
    ASSIGN_TO_ME_BUTTON = (By.CSS_SELECTOR, "#j_assignToMe")
    SAVE_BUTTON = (By.XPATH, "//input[@id='save']")


class TaskViewLocators:
    INFO_BOX = (By.CSS_SELECTOR, "div[id='j_info_box'] p")
    TITLE = (By.XPATH, "(//div[@id='text'])[1]")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "#description")
    ENVIRONMENTS_INPUT = (By.CSS_SELECTOR, "#token-input-environments")
    VERSIONS_INPUT = (By.CSS_SELECTOR, "#token-input-versions")
    PRIORITY_SELECT = (By.CSS_SELECTOR, "#priority")
    DEADLINE_INPUT = (By.CSS_SELECTOR, "#dueDate")
    ASSIGN_TO_ME_BUTTON = (By.CSS_SELECTOR, "#j_assignToMe")
    SAVE_BUTTON = (By.XPATH, "//input[@id='save']")
