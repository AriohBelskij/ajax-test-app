from appium.webdriver.common.appiumby import AppiumBy


class IndexLocator:
    LOGIN_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/login")
    SIGN_UP_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/registration")


class LoginPageLocator:
    EMAIL_FIELD = (AppiumBy.ID, "com.ajaxsystems:id/login")
    PASSWORD_FIELD = (AppiumBy.ID, "com.ajaxsystems:id/password")
    FORGOT_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/forgot")
    AGREEMENT_POLICY = (AppiumBy.ID, "com.ajaxsystems:id/agreementText")
    SUBMIT_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/next")


class HomePageLocator:
    ADD_HUB_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/hubAdd")
    MENU_DRAWER = (AppiumBy.ID, "com.ajaxsystems:id/menuDrawer")


class MenuLocator:
    ADD_HUB_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/addHub")
    SETTINGS_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/settings")
    HELP_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/help")
    REPORT_PROBLEM = (AppiumBy.ID, "com.ajaxsystems:id/logs")
    TERMS_SERVICE = (AppiumBy.ID, "com.ajaxsystems:id/documentation_text")
