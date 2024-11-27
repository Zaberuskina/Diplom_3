from selenium.webdriver.common.by import By

class ResetPasswordLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "div.input.pr-6.pl-6.input_type_text.input_size_default input[name='name']") #поле email
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")#кнопка "Восстановить пароль"
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]//*[name()='path']") #кнопка скрыть/раскрыть пароль
    RESTORE_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa') and text()='Восстановить']") #кнопка "Восстановить"
    PASSWORD_INPUT = (By.XPATH,
                      "//div[contains(@class, 'input pr-6 pl-6 input_type_password input_size_default')]//input[@name='Введите новый пароль']")#поле "Пароль"
    ACTIVE_PASSWORD_INPUT = (By.CSS_SELECTOR, "div.input.pr-6.pl-6.input_type_text.input_size_default label.input__placeholder.text.noselect.text_type_main-default.input__placeholder-focused")  # активное поле "Пароль"