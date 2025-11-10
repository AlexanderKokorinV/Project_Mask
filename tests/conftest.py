import pytest

@pytest.fixture
def card_numbers():
    return "7000792289606361"

@pytest.fixture
def account_numbers():
    return "73654108430135874305"

@pytest.fixture
def card():
    return "Visa Platinum 7000792289606361"

@pytest.fixture
def account():
    return "Счет 73654108430135874305"

@pytest.fixture
def date_str():
    return "2024-03-11T02:26:18.671407"