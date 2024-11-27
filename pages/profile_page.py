#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.profile_page_locators import ProfilePageLocators
from data import URL_PROFILE, URL_ORDER_HISTORY, URL_LOGIN
class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def click_personal_account_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGIN_PERSONAL_BUTTON_ACCOUNT_USER_AUTHORIZED)
        )
        self.driver.find_element(*ProfilePageLocators.LOGIN_PERSONAL_BUTTON_ACCOUNT_USER_AUTHORIZED).click()
        WebDriverWait(self.driver, 10).until(EC.url_to_be(URL_PROFILE))
    def click_order_history_button(self):
        self.driver.find_element(*ProfilePageLocators.HISTORY_ORDERS_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.url_to_be(URL_ORDER_HISTORY))

    def click_logout_button(self):
        self.driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.url_to_be(URL_LOGIN))


    def get_order_number_from_orders_history(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ProfilePageLocators.LAST_ORDER_NUMBER)
        )
        order_number_element = self.driver.find_element(*ProfilePageLocators.LAST_ORDER_NUMBER)
        return order_number_element.text
