from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.home_page import *
from pages.order_page import *
from locators.base_page_locators import *
from locators.order_page_locators import *
from locators.home_page_locators import *
import pytest


def test_go_to_home_page_click_on_logo_scooter(driver):
    BasePage(driver).click_on_logo_scooter()
    assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'


def test_go_to_ya_page_click_on_logo_ya(driver):
    BasePage(driver).click_on_logo_ya()
    BasePage(driver).change_tab()
    assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
        BasePageLocators.button_find_on_ya)) is not None


@pytest.mark.parametrize("button_order, first_name, second_name, adress, metro_station, phone",
                         [(BasePageLocators.button_order_on_header, first_name_valid, second_name_valid, adress_valid, OrderPageLocators.button_metro_rocossovskiy, phone_valid),
                          (HomePageLocators.button_order_on_middle, first_name_valid_long, second_name_valid_long, adress_valid_short, OrderPageLocators.button_metro_rocossovskiy, phone_valid_start_from_plus)])
def test_success_order(driver, button_order, first_name, second_name, adress, metro_station, phone):
    OrderPage(driver).fill_fields_on_first_order_screen(button_order, first_name, second_name, adress, metro_station, phone)
    OrderPage(driver).fill_fields_on_second_order_screen(OrderPageLocators.button_datepicker, OrderPageLocators.button_rental_day)
    assert WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(OrderPageLocators.button_check_status)) is not None

