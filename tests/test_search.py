from typing import Dict, List

import pytest

from src.search import search_transactions


def test_search_transactions(transactions: List[Dict], search: str) -> None:
    """Тест успешного поиска корректных данных"""
    assert search_transactions(transactions, search) == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.mark.parametrize(
    "transactions, search, expected",
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
            "организации",
            [],
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
            "организации",
            [],
        ),
        ([{}], "организации", []),  # Тест работы функции при пустом словаре
    ],
)
def test_search_transactions_par(transactions: List[Dict], search: str, expected: List[Dict]) -> None:
    """Тест работы функции при различных параметрах, вызывающих ошибку"""
    assert search_transactions(transactions, search) == expected
