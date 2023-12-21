from test.base_test import BaseTest
from src.pages import login_page


class Login(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = login_page.LoginPage(self.driver)

    def test_login_positive(self):
        url_main_page = "http://demo.testarena.pl/"

        self.login_page.login(self.CORRECT_EMAIL, self.CORRECT_PASSWORD)

        self.assertTrue(self.login_page.is_url_match(url_main_page))

    def test_login_negative_incorrect_login_data(self):
        incorrect_password = "badPassword"
        url_login_page = "http://demo.testarena.pl/logowanie"

        self.login_page.login(self.CORRECT_EMAIL, incorrect_password)

        self.assertTrue(self.login_page.is_url_match(url_login_page))
        self.assertTrue(self.login_page.is_incorrect_login_data())
