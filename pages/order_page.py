from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from data import *

class OrderPage:
                  
    def __init__(self, driver):
        self.driver = driver

    def fill_field_first_name(self, first_name):
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(field_first_name)).send_keys(first_name)

    def fill_field_second_name(self, second_name):
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(field_second_name)).send_keys(second_name)

    def fill_field_adress(self, adress):
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(field_adress)).send_keys(adress)

    def fill_field_metro_station(self, metro_station):
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(field_metro_station)).click()
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(metro_station)).click()
 
    def fill_field_phone(self, phone):
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(field_phone)).send_keys(phone)

    def click_on_button_next(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(button_next)).click()

    def fill_field_date_of_delivery(self, date):
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(field_date_of_delivery)).click()
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(date)).click()

    def fill_field_rental_period(self, rental_period):
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(field_rental_period)).click()
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(rental_period)).click()

    def click_on_checkbox(self, checkbox):
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(checkbox)).click()

    def click_on_button_order_on_last_screen(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(button_order_on_last_screen)).click()

    def click_on_button_yes_on_order_screen(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(button_yes_on_order_screen)).click()

    def click_on_button_accept_cookie(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(button_accept_cookie)).click()

    def click_on_logo_scooter(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(logo_scooter)).click()
    


        



