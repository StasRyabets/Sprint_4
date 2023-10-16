from selenium.webdriver.common.by import By


class HomePageLocators:

    button_order_on_header = (
        By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')
    button_order_on_middle = (
        By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]')

    answer_price_and_payment = (
        By.XPATH, "//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или картой.') and not(@hidden)]")
    answer_quantity_of_scooters = (
        By.XPATH, '//p[contains(text(), "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.") and not(@hidden)]')
    answer_rental_duration = (
        By.XPATH, '//p[contains(text(), "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.") and not(@hidden)]')
    answer_order_now = (
        By.XPATH, '//p[contains(text(), "Только начиная с завтрашнего дня. Но скоро станем расторопнее.") and not(@hidden)]')
    answer_pre_closure_or_extension = (
        By.XPATH, '//p[contains(text(), "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.") and not(@hidden)]')
    answer_сharger = (
        By.XPATH, '//p[contains(text(), "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.") and not(@hidden)]')
    answer_cancel = (
        By.XPATH, '//p[contains(text(), "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.") and not(@hidden)]')
    answer_area = (
        By.XPATH, '//p[contains(text(), "Да, обязательно. Всем самокатов! И Москве, и Московской области.") and not(@hidden)]')

    question_price_and_payment = (
        By.XPATH, '//div[contains(text(), "Сколько это стоит? И как оплатить?")]')
    question_quantity_of_scooters = (
        By.XPATH, '//div[contains(text(), "Хочу сразу несколько самокатов! Так можно?")]')
    question_rental_duration = (
        By.XPATH, '//div[contains(text(), "Как рассчитывается время аренды?")]')
    question_order_now = (
        By.XPATH, '//div[contains(text(), "Можно ли заказать самокат прямо на сегодня?")]')
    question_pre_closure_or_extension = (
        By.XPATH, '//div[contains(text(), "Можно ли продлить заказ или вернуть самокат раньше?")]')
    question_сharger = (
        By.XPATH, '//div[contains(text(), "Вы привозите зарядку вместе с самокатом?")]')
    question_cancel = (
        By.XPATH, '//div[contains(text(), "Можно ли отменить заказ?")]')
    question_area = (
        By.XPATH, '//div[contains(text(), "Я жизу за МКАДом, привезёте?")]')
