from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.home_page import *
from pages.order_page import *
from locators import *
import pytest


def test_go_to_home_page_click_on_logo_scooter(driver):
    driver.get('https://qa-scooter.praktikum-services.ru/')
    home_page = HomePage(driver)
    order_page = OrderPage(driver)
    home_page.click_on_button_order_on_home_page(button_order_on_header)
    order_page.click_on_logo_scooter()
    assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'


def test_go_to_ya_page_click_on_logo_yandex(driver):
    driver.get('https://qa-scooter.praktikum-services.ru/')
    home_page = HomePage(driver)
    home_page.click_on_logo_yandex()
    driver.switch_to.window(driver.window_handles[-1])
    assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//button[text()="Найти"]'))) is not None


@pytest.mark.parametrize("button_order, first_name, second_name, adress, metro_station, phone",
                         [(button_order_on_header, first_name_valid, second_name_valid, adress_valid, button_metro_rocossovskiy, phone_valid),
                          (button_order_on_middle, first_name_valid_long, second_name_valid_long, adress_valid_short, button_metro_rocossovskiy, phone_valid_start_from_plus)])
def test_success_order(driver, button_order, first_name, second_name, adress, metro_station, phone):
    driver.get('https://qa-scooter.praktikum-services.ru/')
    home_page = HomePage(driver)
    order_page = OrderPage(driver)
    home_page.click_on_button_accept_cookie()
    home_page.click_on_button_order_on_home_page(button_order)
    order_page.fill_field_first_name(first_name)
    order_page.fill_field_second_name(second_name)
    order_page.fill_field_adress(adress)
    order_page.fill_field_metro_station(metro_station)
    order_page.fill_field_phone(phone)
    order_page.click_on_button_next()
    order_page.fill_field_date_of_delivery(button_datepicker)
    order_page.fill_field_rental_period(button_rental_day)
    order_page.click_on_checkbox(checkbox_black)
    order_page.click_on_button_order_on_last_screen()
    order_page.click_on_button_yes_on_order_screen()
    assert WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]"))) is not None
