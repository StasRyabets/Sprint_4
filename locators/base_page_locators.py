from selenium.webdriver.common.by import By


class BasePageLocators:
    button_find_on_ya = (
        By.XPATH, '//button[text()="Найти"]')
    button_order_on_header = (
        By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')
    button_accept_cookie = (
        By.XPATH, "//button[contains(text(), 'да все привыкли')]")

    logo_scooter = (
        By.XPATH, '//a[contains(@class, "Header_LogoScooter")]/img[@alt="Scooter"]')
    logo_yandex = (
        By.XPATH, '//a[contains(@class, "Header_LogoYandex")]/img[@alt="Yandex"]')
