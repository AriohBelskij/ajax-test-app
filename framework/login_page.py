from .locators import IndexLocator, LoginPageLocator, HomePageLocator

from .page import Page


class LoginPage(Page):
    def user_login(self, email: str, password: str) -> None:
        self.click_element(IndexLocator.LOGIN_BUTTON)
        self.fill_field(LoginPageLocator.EMAIL_FIELD, email)
        self.fill_field(LoginPageLocator.PASSWORD_FIELD, password)
        self.click_element(LoginPageLocator.SUBMIT_BUTTON)

    def user_in_home_page(self) -> bool:
        return self.is_element_present(HomePageLocator.MENU_DRAWER)
