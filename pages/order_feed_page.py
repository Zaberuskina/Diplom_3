from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from selenium.webdriver.support.ui import WebDriverWait
class OrderFeedPage(BasePage):
    def click_order_button(self):
        self.click_to_element(OrderFeedPageLocators.ORDER_BUTTON)

    def is_order_window_displayed(self):
        return self.find_element_with_wait(OrderFeedPageLocators.ORDER_WINDOW).is_displayed()

    def close_order_window(self):
        close_button = self.find_element_with_wait(OrderFeedPageLocators.CLOSE_ORDER_WINDOW_BUTTON)
        self.driver.execute_script("arguments[0].click();", close_button)

    def is_order_number_in_list(self, order_number):
        order_elements = self.find_elements_with_wait(OrderFeedPageLocators.ORDER_LIST)
        for order_element in order_elements:
            order_number_text = order_element.find_element(*OrderFeedPageLocators.ORDER_LIST_NUMBERS).text
            if order_number_text == order_number:
                return True
        return False

    def get_all_time_counter_number(self):
        self.find_element_with_wait(OrderFeedPageLocators.ALL_TIME_COUNTER)
        all_time_counter = self.get_text_from_element(OrderFeedPageLocators.ALL_TIME_COUNTER)
        return all_time_counter

    def is_all_time_counter_increased(self, initial_counter):
        current_counter = self.get_all_time_counter_number()
        return int(current_counter) > int(initial_counter)

    def get_today_counter_number(self):
        self.find_element_with_wait(OrderFeedPageLocators.TODAY_COUNTER)
        today_counter = self.get_text_from_element(OrderFeedPageLocators.TODAY_COUNTER)
        return today_counter


    def is_today_counter_increased(self, initial_counter):
        current_counter = self.get_today_counter_number()
        return int(current_counter) > int(initial_counter)


    def wait_for_order_to_appear(self, order_number):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.is_order_number_in_work_list(order_number)
        )
        return True

    def is_order_number_in_work_list(self, order_number):
        orders_section = self.find_elements_with_wait(OrderFeedPageLocators.IN_WORK_ORDERS)

        for order in orders_section:
            order_text = order.text[1:]
            if order_text == order_number:
                return True
        return False
