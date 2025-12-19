from typing import Dict, List

import pytest

from src.categories import count_categories


def test_count_categories(transactions: List[Dict], descriptions: List) -> None:
    """Тест успешного подсчета и группирования корректных данных"""
    assert count_categories(transactions, descriptions) == {
        "Перевод организации": 2,
        "Перевод со счета на счет": 2,
        "Перевод с карты на карту": 1,
    }


@pytest.mark.parametrize(
    "transactions, descriptions, expected",
    [
        (
            [
                {  # Тест работы функции при отсутствии описания
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
            ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"],
            {},
        ),
        (
            [
                {  # Тест работы функции при отсутствии ключа description
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                }
            ],
            ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"],
            {},
        ),
        (
            [
                {  # Тест работы функции при некорректном вводе описания
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                }
            ],
            ["организ"],
            {},
        ),
        (
            [{}],  # Тест работы функции при пустом словаре
            ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"],
            {},
        ),
    ],
)
def test_count_categories_par(transactions: List[Dict], descriptions: List, expected: Dict) -> None:
    """Тест работы функции при различных параметрах, вызывающих ошибку"""
    assert count_categories(transactions, descriptions) == expected
