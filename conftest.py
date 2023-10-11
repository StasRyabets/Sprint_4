from selenium import webdriver
from pages.home_page import *
from pages.order_page import *
from locators import *
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()