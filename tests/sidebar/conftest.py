import pytest
import time

from framework.login_page import LoginPage
import os
from dotenv import load_dotenv, find_dotenv

from framework.sidebar import Sidebar

load_dotenv(find_dotenv())

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


@pytest.fixture(scope="session")
def user_login_fixture(driver):
    driver.launch_app()
    page = LoginPage(driver)
    page.user_login(EMAIL, PASSWORD)
    time.sleep(5)


@pytest.fixture(scope="function")
def sidebar_fixture(user_login_fixture, driver):
    yield Sidebar(driver)


@pytest.fixture(scope="session", autouse=True)
def end_session(driver):
    yield
    driver.close_app()
