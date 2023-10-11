from selenium.webdriver.support import expected_conditions
from pages.home_page import *
from pages.order_page import *
from locators import *
import pytest

@pytest.mark.parametrize("question, answer",
                         [(question_price_and_payment, answer_price_and_payment),
                          (question_quantity_of_scooters, answer_quantity_of_scooters),
                          (question_rental_duration, answer_rental_duration),
                          (question_order_now, answer_order_now),
                          (question_pre_closure_or_extension, answer_pre_closure_or_extension),
                          (question_сharger, answer_сharger),
                          (question_cancel, answer_cancel),
                          (question_area, answer_area)])
def test_question_on_home_page(driver, question, answer):
    driver.get('https://qa-scooter.praktikum-services.ru/')
    home_page = HomePage(driver)
    home_page.click_on_button_accept_cookie()
    home_page.click_on_question(question)
    assert WebDriverWait(driver, 2).until(expected_conditions.presence_of_all_elements_located(
         (answer))) is not None
