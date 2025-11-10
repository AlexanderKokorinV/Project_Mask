import pytest
from src.widget import mask_account_card, get_date

def test_mask_account_card(card):
    """Тест работы функции в обычном режиме"""
    assert mask_account_card(card) == "Visa Platinum 7000 79** **** 6361"

@pytest.mark.parametrize("card, expected", [
    ("700079228960", "Ошибка"),
    ("700079228960874635672535", "Ошибка"),
    ("abcd792289606361", "Ошибка"),
    ("", "Ошибка"),
    ("Master%ard 7158300734726758", "Ошибка")
])
def test_mask_account_card_par(card, expected):
    assert mask_account_card(card) == expected


def test_mask_account_card(account):
    """Тест работы функции в обычном режиме"""
    assert mask_account_card(account) == "Счет **4305"
