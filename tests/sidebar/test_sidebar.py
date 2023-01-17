import pytest

from framework.locators import HomePageLocator, MenuLocator

@pytest.mark.parametrize(
    "button",[
        pytest.param(
            MenuLocator.SETTINGS_BUTTON,
            id="Settings button in sidebar",
        ),
        pytest.param(
            MenuLocator.ADD_HUB_BUTTON,
            id="add hub button in sidebar",
        ),
        pytest.param(
            MenuLocator.HELP_BUTTON,
            id="help button in sidebar",
        ),
        pytest.param(
            MenuLocator.TERMS_SERVICE,
            id="terms service button in sidebar",
        ),
        pytest.param(
            MenuLocator.REPORT_PROBLEM,
            id="report button in sidebar",
        ), ],
)
def test_button_in_sidebar(sidebar_fixture, button):
    page = sidebar_fixture
    sidebar_fixture.click_element(HomePageLocator.MENU_DRAWER)
    assert page.find_element(button)
