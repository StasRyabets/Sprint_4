from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.order_page import *
from locators.base_page_locators import *
from locators.order_page_locators import *
from locators.home_page_locators import *
import pytest


@pytest.mark.parametrize("button_order, first_name, second_name, adress, metro_station, phone",
                         [(BasePageLocators.button_order_on_header, first_name_valid, second_name_valid, adress_valid, OrderPageLocators.button_metro_rocossovskiy, phone_valid),
                          (HomePageLocators.button_order_on_middle, first_name_valid_long, second_name_valid_long, adress_valid_short, OrderPageLocators.button_metro_rocossovskiy, phone_valid_start_from_plus)])
def test_success_order(driver, button_order, first_name, second_name, adress, metro_station, phone):
    OrderPage(driver).fill_fields_on_first_order_screen(button_order, first_name, second_name, adress, metro_station, phone)
    OrderPage(driver).fill_fields_on_second_order_screen(OrderPageLocators.button_datepicker, OrderPageLocators.button_rental_day)
    assert WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(OrderPageLocators.button_check_status)) is not None

