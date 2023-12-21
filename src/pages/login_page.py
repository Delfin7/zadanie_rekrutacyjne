from base_page import BasePage
from ..locators import LoginPageLocators


class LoginPage(BasePage):
    def login(self, email, password):
        self.fill_input(email, *LoginPageLocators.EMAIL_INPUT)
        self.fill_input(password, *LoginPageLocators.PASSWORD_INPUT)
        self.click_button(*LoginPageLocators.LOGIN_BUTTON)

    def is_incorrect_login_data(self):
        return self.find_element(*LoginPageLocators.INCORRECT_LOGIN_DATA_ERROR)
