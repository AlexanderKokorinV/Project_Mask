from typing import Dict, List

from src.widget import get_date, mask_account_card

transactions = [
    {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    }
]


def format_transaction(transaction: Dict) -> str:
    """Форматируем одну транзакцию в требуемый вид"""
    date_string = transaction.get("date", "")
    if date_string:
        # Преобразовываем дату в требуемый вид
        formatted_date = get_date(date_string)
    else:
        formatted_date = "Дата неизвестна"

    description = transaction.get("description", "Описание отсутствует")

    amount = transaction.get("amount")
    if not amount:  # Если работаем с JSON-форматом
        amount = transaction.get("operationAmount", {}).get("amount", 0.0)

    currency = transaction.get("currency_code")
    if not currency:  # Если работаем с JSON-форматом
        currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", "Валюта не указана")

    masked_from_info = ""
    masked_to_info = ""

    # Форматирование отправителя
    from_info = transaction.get("from", "")
    if from_info:
        # Маскировка номера карты или счета
        masked_from_info = mask_account_card(from_info)

    # Форматирование получателя
    to_info = transaction.get("to", "")
    if to_info:
        # Маскировка номера карты или счета
        masked_to_info = mask_account_card(to_info)

    # Собираем итоговую строку для вывода
    formatted_transaction = (
        f"{formatted_date} {description}\n" f"{masked_from_info} -> {masked_to_info}\n" f"{amount} {currency}\n\n"
    )
    return formatted_transaction


def print_formatted_transactions(transactions: List[Dict]) -> None:
    """Выводим на экран отформатированные транзакции из итогового списка"""
    for transaction in transactions:
        formatted_transaction = format_transaction(transaction)
        print(formatted_transaction)
