from pages.home_page import *
from locators.home_page_locators import *
import pytest

@pytest.mark.parametrize("question, answer",
                         [(HomePageLocators.question_price_and_payment, HomePageLocators.answer_price_and_payment),
                          (HomePageLocators.question_quantity_of_scooters, HomePageLocators.answer_quantity_of_scooters),
                          (HomePageLocators.question_rental_duration, HomePageLocators.answer_rental_duration),
                          (HomePageLocators.question_order_now, HomePageLocators.answer_order_now),
                          (HomePageLocators.question_pre_closure_or_extension, HomePageLocators.answer_pre_closure_or_extension),
                          (HomePageLocators.question_сharger, HomePageLocators.answer_сharger),
                          (HomePageLocators.question_cancel, HomePageLocators.answer_cancel),
                          (HomePageLocators.question_area, HomePageLocators.answer_area)])
def test_question_on_home_page(driver, question, answer):
    HomePage(driver).click_on_question(question)
    assert HomePage(driver).check_element_is_visible(answer) is not None

