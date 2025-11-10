import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_number(card_numbers):
    """Тест работы функции в обычном режиме"""
    assert get_mask_card_number(card_numbers) == "7000 79** **** 6361"

@pytest.mark.parametrize("card_number, expected", [
    ("700079228960", "Ошибка"),
    ("700079228960874635672535", "Ошибка"),
    ("abcd792289606361", "Ошибка"),
    ("", "Ошибка")
])
def test_get_mask_card_number_par(card_number, expected):
    """Тест работы функции при различных параметрах, вызывающих ошибку"""
    assert get_mask_card_number(card_number) == expected

def test_get_mask_account(account_numbers):
    """Тест работы функции в обычном режиме"""
    assert get_mask_account(account_numbers) == "**4305"

@pytest.mark.parametrize("account_number, expected", [
    ("736", "Ошибка"),
    ("70007922896087463567253573654108430135874305", "Ошибка"),
    ("abcd4108430135874305", "Ошибка"),
    ("", "Ошибка")
])
def test_get_mask_account_par(account_number, expected):
    """Тест работы функции при различных параметрах, вызывающих ошибку"""
    assert get_mask_account(account_number) == expected
