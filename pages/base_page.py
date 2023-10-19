from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click_on_element(self, xpath):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.element_to_be_clickable(xpath)).click()

    def send_keys(self, xpath, text):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.element_to_be_clickable(xpath)).send_keys(text)

    def check_element_is_visible(self, xpath):
        return WebDriverWait(self.driver, 2).until(expected_conditions.presence_of_all_elements_located(xpath))

    def change_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def click_on_logo_scooter(self):
        self.open('https://qa-scooter.praktikum-services.ru/')
        self.click_on_element(BasePageLocators.logo_scooter)

    def click_on_logo_ya(self):
        self.open('https://qa-scooter.praktikum-services.ru/')
        self.click_on_element(BasePageLocators.logo_yandex)

