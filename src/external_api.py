import os
from typing import Any, Dict, TypedDict

import requests
from dotenv import load_dotenv


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


load_dotenv()

api_key = os.getenv("API_KEY")  # Получение значения переменной окружения API_KEY из .env-файла


def get_amount_in_rubles(transaction: Transaction) -> Any:
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API (Exchange Rates Data API)
    для получения текущего курса валют и конвертации суммы в рубли.
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    elif transaction["operationAmount"]["currency"]["code"] == "USD" or transaction["operationAmount"]["currency"]["code"] == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={transaction['operationAmount']['currency']['code']}&amount={transaction['operationAmount']['amount']}"
        payload: Dict[str, Any] = {}
        headers = {  # Создание заголовка с токеном доступа API
            "apikey": api_key,
        }
        response = requests.get(url, headers=headers, data=payload)  # Отправка GET-запроса к API
        result = float(response.json()["result"])  # Обработка полученного от API ответа
        return result
