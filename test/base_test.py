from unittest import TestCase
from selenium import webdriver


class BaseTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://demo.testarena.pl/")
        self.CORRECT_EMAIL = "administrator@testarena.pl"
        self.CORRECT_PASSWORD = "sumXQQ72$L"

    def tearDown(self):
        self.driver.close()
