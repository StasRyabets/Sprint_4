from selenium.webdriver.support import expected_conditions
from pages.base_page import *
from locators.base_page_locators import *
import allure 

@allure.title("Checking the transition after clicking on the scooter-logo")
def test_go_to_home_page_click_on_logo_scooter(driver):
    BasePage(driver).click_on_logo_scooter()
    assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

@allure.title("Checking the transition after clicking on the yandex-logo")
def test_go_to_ya_page_click_on_logo_ya(driver):
    BasePage(driver).click_on_logo_ya()
    BasePage(driver).change_tab()
    assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
        BasePageLocators.button_find_on_ya)) is not None
    
