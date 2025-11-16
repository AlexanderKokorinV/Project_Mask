from typing import List, Dict, Generator, Iterator, Any

from pycodestyle import continued_indentation


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator:
    """Функция возвращает итератор, который поочередно выдает транзакции с
    заданной валютой операции"""
    try:
        for transaction in transactions:
            if transaction.get("operationAmount", "Ошибка").get("currency", "Ошибка").get("code", "Ошибка") == currency:
                yield transaction
            elif transaction.get("operationAmount", "Ошибка").get("currency", "Ошибка").get("code", "Ошибка") not in ["USD", "RUB"]:
                raise ValueError("Ошибка")
    except ValueError:
        yield "Ошибка"
    except AttributeError:
        yield "Ошибка"


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator:
    """Функция-генератор, которая принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        transaction_description = transaction.get("description", "Ошибка")
        yield transaction_description


def card_number_generator(start:int, stop:int) -> Generator[str, None, None]:
    """Функция-генератор, которая генерирует номера банковских карт в
    заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    for number in range(start, stop + 1):
        string_number = str(number)
        while len(string_number) < 19:
            string_number = "0" + string_number
        card_number = string_number[:4] + " " + string_number[5:9] + " " + string_number[10:14] + " " + string_number[15:19]
        yield str(card_number)