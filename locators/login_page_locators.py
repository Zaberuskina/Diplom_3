from selenium.webdriver.common.by import By

class LoginPageLocators:
    ELEMENT_EMAIL_LOGIN = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]/input')  # поле Email на странице входа
    ELEMENT_EMAIL_PASSWORD = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]/input[@type="password"]')  # поле "Пароль" на странице входа
    ELEMENT_BUTTON_LOGIN = By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text()="Войти"]' # кнопка "Вход" на странице входа
