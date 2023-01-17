from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver) -> None:
        self.driver = driver

    def is_element_present(self, locator: tuple) -> bool:
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def find_element(self, locator: tuple):
        if not self.is_element_present(locator):
            raise NoSuchElementException(
                f"Element with id {locator[1]} not present"
            )
        return self.driver.find_element(*locator)

    def click_element(self, locator: tuple) -> None:
        element = self.find_element(locator)
        element.click()

    def fill_field(self, locator: tuple, value: str) -> None:
        element = self.find_element(locator)
        element.clear()
        element.send_keys(value)

    def back(self) -> None:
        self.driver.back()
