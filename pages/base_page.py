from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Поиск элементов
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    # Клик по элементу
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    # Клик по элементу с использованием JavaScript
    def click_to_element_js(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].click();", element)

    # Ввод текста
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    # Получение текста элемента
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    # Скролл
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
