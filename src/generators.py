import re
from typing import Any, Dict, Generator, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator:
    """Функция возвращает итератор, который поочередно выдает транзакции с
    заданной валютой операции"""
    try:
        for transaction in transactions:
            if (
                transaction.get("operationAmount", "Ошибка").get("currency", "Ошибка").get("code", "Ошибка")
                == currency
            ):
                yield transaction
            elif transaction.get("operationAmount", "Ошибка").get("currency", "Ошибка").get("code", "Ошибка") not in [
                "USD",
                "RUB",
            ]:
                raise ValueError("Ошибка")
    except ValueError:
        yield "Ошибка"
    except AttributeError:
        yield "Ошибка"


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator:
    """Функция-генератор, которая принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""
    try:
        for transaction in transactions:
            if len(transaction.get("description", "Ошибка")) > 0 and re.fullmatch(
                r"[а-яА-Яa-zA-Z \s-]+", transaction.get("description", "Ошибка")
            ):
                transaction_description = transaction.get("description", "Ошибка")
                yield transaction_description
            else:
                raise ValueError("Ошибка")
    except ValueError:
        yield "Ошибка"
    except AttributeError:
        yield "Ошибка"


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Функция-генератор, которая генерирует номера банковских карт в
    заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    try:
        if start > 0 and stop > 0 and start <= stop:
            if start <= 9999999999999999 and stop <= 9999999999999999:
                for number in range(start, stop + 1):
                    string_number = str(number)
                    while len(string_number) < 19:
                        string_number = "0" + string_number
                    card_number = (
                        string_number[:4]
                        + " "
                        + string_number[5:9]
                        + " "
                        + string_number[10:14]
                        + " "
                        + string_number[15:19]
                    )
                    yield str(card_number)
            else:
                raise ValueError("Неверные значения диапазона")
        else:
            raise ValueError("Неверные значения диапазона")
    except ValueError:
        yield "Неверные значения диапазона"
