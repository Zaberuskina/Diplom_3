from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators

class ResetPasswordPage(BasePage):
    def go_to_reset_password(self):
        self.scroll_to_element(ResetPasswordLocators.RESTORE_PASSWORD_BUTTON)
        self.click_to_element(ResetPasswordLocators.RESTORE_PASSWORD_BUTTON)

    def enter_email(self, email):
        self.add_text_to_element(ResetPasswordLocators.EMAIL_INPUT, email)

    def click_restore_button(self):
        self.scroll_to_element(ResetPasswordLocators.RESTORE_BUTTON)
        self.click_to_element(ResetPasswordLocators.RESTORE_BUTTON)

    def show_hide_password(self):
        self.scroll_to_element(ResetPasswordLocators.SHOW_HIDE_PASSWORD_BUTTON)
        self.click_to_element(ResetPasswordLocators.SHOW_HIDE_PASSWORD_BUTTON)

    def is_password_input_active(self):
        return self.find_element_with_wait(ResetPasswordLocators.ACTIVE_PASSWORD_INPUT).is_displayed()
