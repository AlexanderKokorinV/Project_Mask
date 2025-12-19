import pytest
from src.formatting import format_transaction, print_formatted_transactions


@pytest.mark.parametrize("transaction, expected_substrings", [
    # Тестируем для JSON-формата данных
    (
        {
            "date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        ["26.08.2019", "Перевод организации", "1596 83** **** 5199", "**9589", "31957.58 RUB"]
    ),
    # Тестируем для CSV-формата данных
    (
        {
            "date": "2023-11-12T16:17:52Z",
            "description": "Перевод с карты на карту",
            "amount": "100.00",
            "currency_code": "USD",
            "from": "Visa 2336865385909932",
            "to": "Счет 90621941572206379881"
        },
        ["12.11.2023", "Перевод с карты на карту", "2336 86** **** 9932", "**9881", "100.00 USD"]
    ),
    # Тестируем при отсутствии данных
    (
        {},
        ["Дата неизвестна", "Описание отсутствует", "Валюта не указана"]
    )
])
def test_format_transaction(transaction, expected_substrings):
    """Тест работы функции при различных параметрах"""
    result = format_transaction(transaction)
    for substring in expected_substrings:
        assert substring in result # Проверяем наличие ключевых элементов в итоговом тексте
