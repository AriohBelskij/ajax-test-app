from framework import LoginPage
from framework.locators import HomePageLocator


class Sidebar(LoginPage):
    def open_draw_menu(self) -> None:
        self.click_element(HomePageLocator.MENU_DRAWER)
