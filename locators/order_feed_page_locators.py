from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    ORDER_BUTTON  = By.XPATH, "//p[contains(@class, 'text_type_digits-default')]"#кнопка оформить заказ
    ORDER_WINDOW = By.XPATH, "//div[contains(@class,'Modal_orderBox__1xWdi')]"#окно заказа

    ORDER_NUMBER = (By.XPATH, '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')#номер заказа
    CLOSE_ORDER_WINDOW_BUTTON = By.XPATH, "//button[@type='button']"  # кнопка закрытия окна заказа

    ORDER_LIST = By.CSS_SELECTOR, 'ul.OrderFeed_list__OLh59 > li'
    ORDER_LIST_NUMBERS = By.CSS_SELECTOR, '.text.text_type_digits-default'

    ALL_TIME_COUNTER = By.XPATH, "//div[p[text()='Выполнено за все время:']]/p[2]"
    TODAY_COUNTER = By.XPATH, "//div[p[text()='Выполнено за сегодня:']]/p[2]"
    IN_WORK_ORDERS = By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi li"


