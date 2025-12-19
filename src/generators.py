from typing import Dict, Generator, Iterator, List

from src.operations import PATH_TO_CSV_FILE, PATH_TO_EXCEL_FILE, get_operations_from_csv, get_operations_from_excel
from src.utils import PATH_TO_JASON_FILE, get_transactions_from_json

transactions_json = get_transactions_from_json(PATH_TO_JASON_FILE)
transactions_csv = get_operations_from_csv(PATH_TO_CSV_FILE)
transactions_excel = get_operations_from_excel(PATH_TO_EXCEL_FILE)


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator:
    """Функция возвращает итератор, который поочередно выдает транзакции с
    заданной валютой операции"""
    if not isinstance(transactions, list):
        return iter([])  # Если входные данные не список, возвращаем пустой итератор

    for transaction in transactions:
        try:
            currency_code = transaction["operationAmount"]["currency"]["code"]
            if currency_code == currency:
                yield transaction
        except KeyError:
            continue
        except ValueError:
            continue
        except AttributeError:
            continue


def transaction_descriptions(transactions: List[Dict]) -> Iterator:
    """Функция-генератор, которая принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""
    if not isinstance(transactions, list):  # Если входные данные не являются списком, завершаем работу
        return

    for transaction in transactions:
        if not isinstance(transaction, dict):  # Проверяем, что transaction — это словарь
            continue

        description = transaction.get("description", "")

        if (
            isinstance(description, str) and description.strip()
        ):  # Проверяем, что описание — это строка и она не пустая
            yield description.strip()


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Функция-генератор, которая генерирует номера банковских карт в
    заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    if not (1 <= start <= stop <= 9999_9999_9999_9999):
        return

    for number in range(start, stop + 1):
        s = f"{number:016}"  # Cоздаем строку из 16 символов с нулями в начале
        card_number = f"{s[0:4]} {s[4:8]} {s[8:12]} {s[12:16]}"  # Разбиваем на блоки по 4 цифры
        yield card_number
