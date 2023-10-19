from pages.base_page import BasePage
from locators.order_page_locators import *
from locators.base_page_locators import *
from data import *


class OrderPage(BasePage):

    def fill_fields_on_first_order_screen(self, button_order, first_name, second_name, adress, metro_station, phone):
        self.open('https://qa-scooter.praktikum-services.ru/')
        self.click_on_element(BasePageLocators.button_accept_cookie)
        self.click_on_element(button_order)
        self.send_keys(OrderPageLocators.field_first_name, first_name)
        self.send_keys(OrderPageLocators.field_second_name, second_name)
        self.send_keys(OrderPageLocators.field_adress, adress)
        self.click_on_element(OrderPageLocators.field_metro_station)
        self.click_on_element(metro_station)
        self.send_keys(OrderPageLocators.field_phone, phone)
        self.click_on_element(OrderPageLocators.button_next)

    def fill_fields_on_second_order_screen(self, date, rental_period):
        self.click_on_element(OrderPageLocators.field_date_of_delivery)
        self.click_on_element(date)
        self.click_on_element(OrderPageLocators.field_rental_period)
        self.click_on_element(rental_period)
        self.click_on_element(OrderPageLocators.checkbox_black)
        self.click_on_element(OrderPageLocators.button_order_on_last_screen)
        self.click_on_element(OrderPageLocators.button_yes_on_order_screen)

