from selenium.webdriver.common.by import By

class ProfilePageLocators:
    LOGIN_PERSONAL_BUTTON_ACCOUNT_USER_AUTHORIZED = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX"]//p[text()="Личный Кабинет"]')  # Кнопка "Личный Кабинет"
    HISTORY_ORDERS_BUTTON = (By.XPATH, '//a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive" and text()="История заказов"]')  # Кнопка "История заказов"
    LOGOUT_BUTTON = (By.XPATH, '//button[@type="button" and @class="Account_button__14Yp3 text text_type_main-medium text_color_inactive" and text()="Выход"]')  # Кнопка "Выход"

    LAST_ORDER_NUMBER = (By.XPATH,
                         '//li[@class="OrderHistory_listItem__2x95r mb-6"][last()]//p[@class="text text_type_digits-default"]')  # Номер последнего заказа