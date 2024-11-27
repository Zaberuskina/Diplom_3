import pytest
import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeedPage
from data import URL_ORDER_FEED, URL_CONSTRUCTOR
import time
from locators.main_page_locators import MainPageLocators

class TestOrderFeedPage:

    @allure.title("Проверка отображения окна заказа")
    @allure.description("Тест проверяет, что при нажатии на кнопку 'Оформить заказ' появляется окно заказа")
    @pytest.mark.usefixtures("driver")
    def test_order_window(self, driver):
        order_feed_page = OrderFeedPage(driver)
        driver.get(URL_ORDER_FEED)

        with allure.step("Нажать на кнопку 'Оформить заказ'"):
            order_feed_page.click_order_button()

        with allure.step("Проверка отображения окна заказа"):
            assert order_feed_page.is_order_window_displayed()

    @allure.title("Проверка отображения заказов пользователя на странице ленты заказов")
    @allure.description("Тест проверяет, что заказы пользователя из раздела 'История заказов' отображаются на странице 'Лента заказов'")
    @pytest.mark.usefixtures("authorization")
    def test_order_feed_page(self, driver):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Создать заказ"):
            main_page.create_order()

        with allure.step("Закрыть окно с заказом"):
            order_feed_page.close_order_window()
        time.sleep(5)
        with allure.step("Перейти в личный кабинет"):
            profile_page.click_personal_account_button()

        with allure.step("Перейти в историю заказов"):
            profile_page.click_order_history_button()

        with allure.step("Получить номер последнего заказа из истории заказов"):
            created_order_number = profile_page.get_order_number_from_orders_history()

        with allure.step("Перейти на страницу ленты заказов"):
            driver.get(URL_ORDER_FEED)

        with allure.step("Проверить, что номер заказа отображается в ленте заказов"):
            order_number_is_in_list = order_feed_page.is_order_number_in_list(created_order_number)
            assert order_number_is_in_list

    @allure.title('Создание заказа увеличивает общий счетчик заказов')
    @allure.description('После создания нового заказа общий счетчик заказов в ленте заказов увеличивается.')
    @pytest.mark.usefixtures("authorization")
    def test_creating_order_all_time_counter(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Перейти в ленту заказов"):
            main_page.go_to_order_feed()

        with allure.step("Получить начальное значение счетчика заказов"):
            initial_counter = order_feed_page.get_all_time_counter_number()

        with allure.step("Перейти на страницу конструктора"):
            driver.get(URL_CONSTRUCTOR)

        with allure.step("Перетащить ингредиент"):
            main_page.drag_and_drop_ingredient()

        with allure.step("Нажать кнопку 'Оформить заказ'"):
            order_button = main_page.find_element_with_wait(MainPageLocators.ORDER_BUTTON)
            order_button.click()

        with allure.step("Закрыть окно с заказом"):
            order_feed_page.close_order_window()
        time.sleep(5)
        with allure.step("Перейти в ленту заказов"):
            main_page.go_to_order_feed()

        with allure.step("Проверить, что счетчик заказов увеличился"):
            all_time_counter_increased = order_feed_page.is_all_time_counter_increased(initial_counter)
            assert all_time_counter_increased, f"Order counter did not increase. Initial: {initial_counter}, Current: {order_feed_page.get_all_time_counter_number()}"

    @allure.title('Создание заказа увеличивает счетчик выполненных заказов за сегодня')
    @allure.description('После создания нового заказа счетчик выполненных заказов за сегодня увеличивается.')
    @pytest.mark.usefixtures("authorization")
    def test_creating_order_day_counter(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Перейти в ленту заказов"):
            main_page.go_to_order_feed()

        with allure.step("Получить начальное значение счетчика заказов за сегодня"):
            initial_counter = order_feed_page.get_today_counter_number()

        with allure.step("Перейти на страницу конструктора"):
            driver.get(URL_CONSTRUCTOR)

        with allure.step("Перетащить ингредиент"):
            main_page.drag_and_drop_ingredient()

        with allure.step("Нажать кнопку 'Оформить заказ'"):
            order_button = main_page.find_element_with_wait(MainPageLocators.ORDER_BUTTON)
            order_button.click()

        with allure.step("Закрыть окно с заказом"):
            order_feed_page.close_order_window()
        time.sleep(5)
        with allure.step("Перейти в ленту заказов"):
            main_page.go_to_order_feed()

        with allure.step("Проверить, что счетчик заказов за сегодня увеличился"):
            today_counter_increased = order_feed_page.is_today_counter_increased(initial_counter)
            assert today_counter_increased, f"Order counter did not increase. Initial: {initial_counter}, Current: {order_feed_page.get_today_counter_number()}"

    @allure.title('Созданный заказ отображается в разделе "В работе"')
    @allure.description('После создания заказа, он отображается в разделе "В работе" ленты заказов.')
    @pytest.mark.usefixtures("authorization")
    def test_created_order_work(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Создать заказ"):
            main_page.create_order()

        with allure.step("Закрыть окно с заказом"):
            order_feed_page.close_order_window()
        time.sleep(5)
        with allure.step("Перейти в ленту заказов"):
            main_page.go_to_order_feed()

        with allure.step("Получить номер заказа"):
            order_number = order_feed_page.get_all_time_counter_number()

        with allure.step("Ожидание появления заказа в списке заказов 'В работе'"):
            order_feed_page.wait_for_order_to_appear(order_number)

        with allure.step("Проверить наличие номера заказа в списке 'В работе'"):
            assert order_feed_page.is_order_number_in_work_list(order_number), f"Order number {order_number} not found in the 'In Work' list"
