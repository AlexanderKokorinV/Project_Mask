from typing import List, Dict, Generator


def filter_by_currency(transactions: List[Dict], currency: str) -> Generator[Dict]:
    """Функция возвращает итератор, который поочередно выдает транзакции с
    заданной валютой операции"""
    for transaction in transactions:
        if transaction.get("operationAmount").get("currency").get("code") == currency:
            yield transaction

def transaction_descriptions(transactions: List[Dict]) -> Generator[str]:
    """Функция-генератор, которая принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        transaction_description = transaction.get("description")
        yield transaction_description


def card_number_generator(start:int, stop:int) -> Generator[str]:
    """Функция-генератор, которая генерирует номера банковских карт в
    заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    for number in range(start, stop + 1):
        string_number = str(number)
        while len(string_number) < 19:
            string_number = "0" + string_number
        card_number = string_number[:4] + " " + string_number[5:9] + " " + string_number[10:14] + " " + string_number[15:19]
        yield str(card_number)