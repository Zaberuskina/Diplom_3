import pytest
import allure
from pages.reset_password_page import ResetPasswordPage
from data import EMAIL, URL_LOGIN

class TestResetPasswordPage:

    @allure.title("Тест восстановления пароля")
    @allure.description("Тест проверяет процесс восстановления пароля и отображение поля пароля")
    def test_reset_password(self, driver):
        driver.get(URL_LOGIN)
        reset_password_page = ResetPasswordPage(driver)

        with allure.step("Нажать на кнопку 'Восстановить пароль'"):
            reset_password_page.go_to_reset_password()

        with allure.step("Ввести email"):
            reset_password_page.enter_email(EMAIL)

        with allure.step("Нажать на кнопку 'Восстановить'"):
            reset_password_page.click_restore_button()

        with allure.step("Проверить, что при нажатии на кнопку 'Скрыть/раскрыть пароль' поле 'Пароль' становится активным и подсвечивается"):
            reset_password_page.show_hide_password()
            assert reset_password_page.is_password_input_active()
