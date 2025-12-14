import os
from typing import Any, Dict, TypedDict
from unittest.mock import Mock, patch

from src.external_api import get_amount_in_rubles


class Currency(TypedDict):
    name: str
    code: str


class OperationAmount(TypedDict):
    amount: str
    currency: Currency


class Transaction(TypedDict):
    id: int
    state: str
    date: str
    operationAmount: OperationAmount
    description: str
    from_: str
    to: str


TRANSACTION_EUR: Transaction = {  # Mock-данные, которые мы будем использовать в тестах
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}},
    "description": "Перевод организации",
    "from_": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702",
}

TRANSACTION_USD: Transaction = {  # Mock-данные, которые мы будем использовать в тестах
    "id": 716496732,
    "state": "EXECUTED",
    "date": "2018-04-04T17:33:34.701093",
    "operationAmount": {"amount": "40701.91", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from_": "Visa Gold 5999414228426353",
    "to": "Счет 72731966109147704472",
}


@patch("src.external_api.requests.get")
def test_get_amount_in_rubles_eur(mock_get: Mock, account_numbers: str) -> None:
    """Тест работы функции при конвертации суммы из евро в рубли"""
    mock_response = Mock()  # Мокируем ответ API
    expected_result_amount = 889483.518943
    mock_response.json.return_value = {
        "result": expected_result_amount
    }  # Функция json() мок-объекта возвращает словарь с ключом "result"
    mock_get.return_value = mock_response  # Устанавливаем мок-ответ для requests.get

    # Вычисляем ожидаемые URL, headers и payload, которые использует функция
    expected_amount = TRANSACTION_EUR["operationAmount"]["amount"]
    expected_url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={expected_amount}"
    expected_headers = {"apikey": os.getenv("API_KEY")}  # Используем реальный API_KEY из env
    expected_payload: Dict[str, Any] = {}

    result = get_amount_in_rubles(TRANSACTION_EUR)
    assert result == expected_result_amount

    # Проверяем, что requests.get был вызван только один раз с заданными аргументами
    mock_get.assert_called_once_with(expected_url, headers=expected_headers, data=expected_payload)


@patch("src.external_api.requests.get")
def test_get_amount_in_rubles_usd(mock_get: Mock, account_numbers: str) -> None:
    """Тест работы функции при конвертации суммы из долларов в рубли"""
    mock_response = Mock()  # Мокируем ответ API
    expected_result_amount = 3195140.95
    mock_response.json.return_value = {
        "result": expected_result_amount
    }  # Функция json() мок-объекта возвращает словарь с ключом "result"
    mock_get.return_value = mock_response  # Устанавливаем мок-ответ для requests.get

    # Вычисляем ожидаемые URL, headers и payload, которые использует функция
    expected_amount = TRANSACTION_USD["operationAmount"]["amount"]
    expected_url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={expected_amount}"
    expected_headers = {"apikey": os.getenv("API_KEY")}  # Используем реальный API_KEY из env
    expected_payload: Dict[str, Any] = {}

    result = get_amount_in_rubles(TRANSACTION_USD)
    assert result == expected_result_amount

    # Проверяем, что requests.get был вызван только один раз с заданными аргументами
    mock_get.assert_called_once_with(expected_url, headers=expected_headers, data=expected_payload)


def test_get_amount_in_rubles_rub(transaction_rub: Transaction) -> None:
    """Тест работы функции при обработке рублевых транзакций"""
    assert get_amount_in_rubles(transaction_rub) == 97853.86
