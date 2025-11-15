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