from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import URL_CONSTRUCTOR, URL_ORDER_FEED
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def go_to_constructor(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(URL_CONSTRUCTOR))

    def go_to_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(URL_ORDER_FEED))

    def open_ingredient_details(self):
        self.click_to_element(MainPageLocators.INGREDIENT_ADD_BUTTON)
        return self.find_element_with_wait(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    def close_ingredient_details(self):
        self.click_to_element(MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)
        return self.find_element_with_wait(MainPageLocators.INGREDIENT_ADD_BUTTON)

    def drag_and_drop_ingredient(self):
        ingredient_add_button = self.find_element_with_wait(MainPageLocators.INGREDIENT_ADD_BUTTON)
        top_bun_text = self.find_element_with_wait(MainPageLocators.TOP_BUN_TEXT)
        self.driver.execute_script(
            "function createEvent(typeOfEvent) {\n"
            "var event = document.createEvent(\"CustomEvent\");\n"
            "event.initCustomEvent(typeOfEvent, true, true, null);\n"
            "event.dataTransfer = {\n"
            "data: {},\n"
            "setData: function (key, value) {\n"
            "this.data[key] = value;\n"
            "},\n"
            "getData: function (key) {\n"
            "return this.data[key];\n"
            "}\n"
            "};\n"
            "return event;\n"
            "}\n"
            "\n"
            "function dispatchEvent(element, event, transferData) {\n"
            "if (transferData !== undefined) {\n"
            "event.dataTransfer = transferData;\n"
            "}\n"
            "if (element.dispatchEvent) {\n"
            "element.dispatchEvent(event);\n"
            "} else if (element.fireEvent) {\n"
            "element.fireEvent(\"on\" + event.type, event);\n"
            "}\n"
            "}\n"
            "\n"
            "function simulateHTML5DragAndDrop(element, destination) {\n"
            "var dragStartEvent = createEvent('dragstart');\n"
            "dispatchEvent(element, dragStartEvent);\n"
            "var dropEvent = createEvent('drop');\n"
            "dispatchEvent(destination, dropEvent, dragStartEvent.dataTransfer);\n"
            "var dragEndEvent = createEvent('dragend');\n"
            "dispatchEvent(element, dragEndEvent, dropEvent.dataTransfer);\n"
            "}\n"
            "\n"
            "var source = arguments[0];\n"
            "var destination = arguments[1];\n"
            "simulateHTML5DragAndDrop(source, destination);",
            ingredient_add_button, top_bun_text
        )

    def get_counter_value(self):
        counter_element = self.find_element_with_wait(MainPageLocators.COUNTER)
        return int(counter_element.text)

    def create_order(self):
        self.go_to_constructor()
        self.drag_and_drop_ingredient()
        order_button = self.find_element_with_wait(MainPageLocators.ORDER_BUTTON)
        order_button.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.ORDER_STATUS))
        return self.find_element_with_wait(MainPageLocators.ORDER_STATUS)

    def wait_page_to_be_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(URL_CONSTRUCTOR))


