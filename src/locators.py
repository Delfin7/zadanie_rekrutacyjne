from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login")
    INCORRECT_LOGIN_DATA_ERROR = (By.CSS_SELECTOR, ".login_form_error")


class DashboardPageLocators:
    TASKS_BUTTON = (By.CSS_SELECTOR, "a[href='http://demo.testarena.pl/zK/tasks']")
    CHANGE_PROJECT_LIST = (By.CSS_SELECTOR, "#activeProject_chosen > a")
    PROJECT_SELECT = (By.CSS_SELECTOR, "#activeProject_chosen > div > div > input[type=text]")


class TasksPageLocators:
    ADD_A_TASK_BUTTON = (By.CSS_SELECTOR, ".button_link")


class AddTaskPageLocators:
    TITLE_INPUT = (By.CSS_SELECTOR, "#title")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "#description")
    ENVIRONMENTS_INPUT = (By.CSS_SELECTOR, "#token-input-environments")
    ENVIRONMENTS_LIST = (By.XPATH, "/html/body/div[4]/ul/li")
    VERSIONS_INPUT = (By.CSS_SELECTOR, "#token-input-versions")
    VERSIONS_LIST = (By.XPATH, "/html/body/div[5]/ul/li")
    DEADLINE_INPUT = (By.CSS_SELECTOR, "#dueDate")
    ASSIGN_TO_ME_BUTTON = (By.CSS_SELECTOR, "#j_assignToMe")
    SAVE_BUTTON = (By.XPATH, "//input[@id='save']")


class TaskViewLocators:
    INFO_BOX = (By.CSS_SELECTOR, "div[id='j_info_box'] p")
    TITLE = (By.XPATH, "(//div[@id='text'])[1]")
    DESCRIPTION = (By.XPATH, '//*[@id="content"]/article/div[2]/div[1]/div[2]/div')
    ENVIRONMENTS = (By.XPATH, '//*[@id="text"]/a')
    VERSIONS = (By.XPATH, '//*[@id="text"]/a')
    DEADLINE = (By.XPATH, '/html/body/div[2]/section/article/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]')
