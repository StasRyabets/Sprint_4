from pages.base_page import BasePage
from locators.home_page_locators import *
from locators.base_page_locators import *
from data import *


class HomePage(BasePage):

    def click_on_question(self, question):
        self.open('https://qa-scooter.praktikum-services.ru/')
        self.click_on_element(BasePageLocators.button_accept_cookie)
        self.click_on_element(question)

