import pytest
import allure
from pages.main_page import MainPage
from data import URL_CONSTRUCTOR, URL_ORDER_FEED

class TestMainPage:

    @allure.title("Переход на страницу конструктора")
    @allure.description("Тест проверяет переход на страницу конструктора")
    @pytest.mark.usefixtures("authorization")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        with allure.step("Клик на кнопку 'Конструктор'"):
            main_page.go_to_constructor()
        with allure.step("Проверка URL"):
            assert driver.current_url == URL_CONSTRUCTOR

    @allure.title("Переход на страницу ленты заказов")
    @allure.description("Тест проверяет переход на страницу ленты заказов")
    @pytest.mark.usefixtures("authorization")
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        with allure.step("Клик на кнопку 'Лента заказов'"):
            main_page.go_to_order_feed()
        with allure.step("Проверка URL"):
            assert driver.current_url == URL_ORDER_FEED

    @allure.title("Проверка всплывающего окна деталей ингредиента")
    @allure.description("Тест проверяет отображение всплывающего окна деталей ингредиента")
    @pytest.mark.usefixtures("authorization")
    def test_ingredient_details_popup(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открыть всплывающее окно деталей ингредиента"):
            ingredient_details_popup = main_page.open_ingredient_details()
        with allure.step("Проверка отображения всплывающего окна"):
            assert ingredient_details_popup.is_displayed()
        with allure.step("Закрытие всплывающего окна"):
            ingredient_add_button = main_page.close_ingredient_details()
        with allure.step("Проверка отображения ингредиента"):
            assert ingredient_add_button.is_displayed()

    @allure.title("Проверка счетчика ингредиентов")
    @allure.description("Тест проверяет, что счетчик ингредиентов больше нуля после добавления ингредиента")
    @pytest.mark.usefixtures("authorization")
    def test_counter(self, driver):
        main_page = MainPage(driver)
        with allure.step("Перетащить ингредиент"):
            main_page.drag_and_drop_ingredient()
        with allure.step("Проверка счетчика - счетчик больше нуля"):
            counter_value = main_page.get_counter_value()
            assert counter_value > 0, f"Expected counter to be greater than 0, but got {counter_value}"

    @allure.title("Проверка создания заказа, когда пользователь авторизован")
    @allure.description("Тест проверяет создание заказа и отображение статуса заказа")
    @pytest.mark.usefixtures("authorization")
    def test_order(self, driver):
        main_page = MainPage(driver)
        with allure.step("Создать заказ"):
            order_status_element = main_page.create_order()
        with allure.step("Проверка отображения статуса заказа"):
            assert order_status_element.is_displayed()
