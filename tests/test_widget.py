import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(card):
    """Тест работы функции в обычном режиме"""
    assert mask_account_card(card) == "Visa Platinum 7000 79** **** 6361"


@pytest.mark.parametrize(
    "card, expected",
    [
        ("700079228960", "Ошибка"),
        ("700079228960874635672535", "Ошибка"),
        ("abcd792289606361", "Ошибка"),
        ("", "Ошибка"),
        ("Master%ard 7158300734726758", "Ошибка"),
    ],
)
def test_mask_account_card_par(card, expected):
    """Тест работы функции при различных параметрах, вызывающих ошибку"""
    assert mask_account_card(card) == expected


def test_mask_account(account):
    """Тест работы функции в обычном режиме для банковского счета"""
    assert mask_account_card(account) == "Счет **4305"


@pytest.mark.parametrize(
    "account_number, expected",
    [("736", "Ошибка"), ("70007922896087463567253573654108430135874305", "Ошибка"), ("", "Ошибка")],
)
def test_mask_account_par(account_number, expected):
    """Тест работы функции для банковского счета при различных параметрах, вызывающих ошибку"""
    assert mask_account_card(account_number) == expected


def test_get_date(date_str):
    """Тест работы функции в обычном режиме"""
    assert get_date(date_str) == "11.03.2024"


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("736", "Ошибка"),
        ("70007922896087463567253573654108430135874305", "Ошибка"),
        ("2024-0sEdfT02:26:18.671407", "Ошибка"),
        ("", "Ошибка"),
    ],
)
def test_get_date_par(date_str, expected):
    """Тест работы функции при различных параметрах, вызывающих ошибку"""
    assert get_date(date_str) == expected
