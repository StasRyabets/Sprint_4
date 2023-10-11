from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from data import *


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_button_accept_cookie(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.element_to_be_clickable(button_accept_cookie)).click()

    def click_on_logo_yandex(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.element_to_be_clickable(logo_yandex)).click()

    def click_on_button_order_on_home_page(self, button):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.element_to_be_clickable(button)).click()

    def click_on_question(self, question):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.element_to_be_clickable(question)).click()

    def check_answer(self, answer):
        WebDriverWait(self.driver, 2).until(expected_conditions.presence_of_element_located(answer))