from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo" and @href="/" and .//p[text()="Конструктор"]]')  # Кнопка "Конструктор"
    ORDER_FEED_BUTTON = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/feed" and .//p[text()="Лента Заказов"]]')  # Кнопка "Лента Заказов"
    INGREDIENT_DETAILS_POPUP = (By.XPATH, '//div[@class="Modal_modal__contentBox__sCy8X pt-10 pb-15" and .//h2[text()="Детали ингредиента"]]')  # Всплывающее окно деталей ингредиента
    INGREDIENT_DETAILS_CLOSE_BUTTON = (By.XPATH, '//section[contains(@class,"Modal_modal_opened")]//button[@type="button"]')  # Кнопка закрытия всплывающего окна деталей ингредиента
    INGREDIENT_ADD_BUTTON = (By.XPATH, '//a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href="/ingredient/61c0c5a71d1f82001bdaaa6d" and .//p[text()="Флюоресцентная булка R2-D3"]]')  # Кнопка ингредиента
    TOP_BUN_TEXT = (By.XPATH, '//span[@class="constructor-element__text" and text()="Перетяните булочку сюда (верх)"]')  # Текст для перетаскивания верхней булочки
    COUNTER = (By.XPATH, '//div[@class="BurgerConstructor_basket__totalContainer__2Z-ho mr-10"]//p[@class="text text_type_digits-medium mr-3"]')  # Счетчик ингредиентов
    ORDER_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg" and text()="Оформить заказ"]')  # Кнопка "Оформить заказ"
    ORDER_STATUS = (By.XPATH, '//p[@class="undefined text text_type_main-small mb-2" and text()="Ваш заказ начали готовить"]')  # Текст со статусом заказа