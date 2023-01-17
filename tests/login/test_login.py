import pytest
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


@pytest.mark.parametrize(
    "email,password,expected",
    [
        pytest.param(
            EMAIL,
            PASSWORD,
            True,
            id="test with correct login data",
        ),
        pytest.param(
            "wrong@email.com",
            "wrong_password",
            False,
            id="test with wrong login data",
        ),
        pytest.param(
            EMAIL,
            "wrong_password",
            False,
            id="Test with wrong pass",
        ),
        pytest.param(
            "wrong@email.com",
            PASSWORD,
            False,
            id="Test with wrong email",
        ),
        pytest.param(
            EMAIL,
            " ",
            False,
            id="Test with empty pass field",
        ),
        pytest.param(
            " ",
            PASSWORD,
            False,
            id="Test with empty email field",
        ),
        pytest.param(" ", " ", False, id="Test with empty fields"),
    ],
)
def test_user_login(user_login_fixture, email, password, expected):
    page = user_login_fixture
    page.user_login(email, password)
    assert page.user_in_home_page() == expected
