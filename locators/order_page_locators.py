from selenium.webdriver.common.by import By


class OrderPageLocators:

    button_next = (By.XPATH, '//button[contains(text(), "Далее")]')
    button_metro_rocossovskiy = (
        By.XPATH, '//button[contains(@class, "Order_SelectOption") and div[text()="Бульвар Рокоссовского"]]')
    button_rental_day = (
        By.XPATH, '//div[contains(@class, "Dropdown-option") and text()="сутки"]')
    button_order_on_last_screen = (
        By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]')
    button_yes_on_order_screen = (By.XPATH, '//button[contains(text(), "Да")]')
    button_accept_cookie = (
        By.XPATH, "//button[contains(text(), 'да все привыкли')]")

    logo_scooter = (
        By.XPATH, '//a[contains(@class, "Header_LogoScooter")]/img[@alt="Scooter"]')
    logo_yandex = (
        By.XPATH, '//a[contains(@class, "Header_LogoYandex")]/img[@alt="Yandex"]')

    button_datepicker = (
        By.XPATH, '//div[contains(@class, "react-datepicker__day--001")]')

    checkbox_black = (By.XPATH, "//label[contains(text(), 'чёрный жемчуг')]")

    field_first_name = (By.XPATH, '//input[@placeholder="* Имя"]')
    field_second_name = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    field_adress = (
        By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    field_metro_station = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    field_phone = (
        By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    field_date_of_delivery = (
        By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    field_rental_period = (
        By.XPATH, '//div[contains(@class, "Dropdown-placeholder") and text()="* Срок аренды"]')
