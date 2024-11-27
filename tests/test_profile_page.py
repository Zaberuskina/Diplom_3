import pytest
import allure
from pages.profile_page import ProfilePage
from data import URL_PROFILE, URL_ORDER_HISTORY, URL_LOGIN

class TestProfilePage:

    @allure.title("Тест страницы профиля")
    @allure.description("Тест проверяет переходы между страницами профиля, истории заказов и выхода из аккаунта")
    @pytest.mark.usefixtures("authorization")
    def test_profile_page(self, driver):
        profile_page = ProfilePage(driver)

        with allure.step("Нажать на кнопку 'Личный Кабинет'"):
            profile_page.click_personal_account_button()
            assert driver.current_url == URL_PROFILE

        with allure.step("Нажать на кнопку 'История заказов'"):
            profile_page.click_order_history_button()
            assert driver.current_url == URL_ORDER_HISTORY

        with allure.step("Нажать на кнопку 'Выход'"):
            profile_page.click_logout_button()
            assert driver.current_url == URL_LOGIN
