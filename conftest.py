import pytest
from selenium import webdriver
from data import DRIVER_NAME
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import DRIVER_NAME, EMAIL, PASSWORD, URL_LOGIN

@pytest.fixture(scope="function")
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def firefox():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    global DRIVER_NAME
    if request.param == 'chrome':
        DRIVER_NAME = 'chrome'
        yield request.getfixturevalue('chrome')
    else:
        DRIVER_NAME = 'firefox'
        yield request.getfixturevalue('firefox')

@pytest.fixture()
def authorization(driver):
    driver.get(URL_LOGIN)
    driver.find_element(*LoginPageLocators.ELEMENT_EMAIL_LOGIN).send_keys(EMAIL)
    driver.find_element(*LoginPageLocators.ELEMENT_EMAIL_PASSWORD).send_keys(PASSWORD)

    # Ожидание, пока кнопка ELEMENT_BUTTON_LOGIN станет кликабельной
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.ELEMENT_BUTTON_LOGIN)
    )

    # Использование JavaScript для клика на кнопку
    login_button = driver.find_element(*LoginPageLocators.ELEMENT_BUTTON_LOGIN)
    driver.execute_script("arguments[0].click();", login_button)

    WebDriverWait(driver, 10).until(
        EC.url_to_be(URL_LOGIN)
    )
    return driver