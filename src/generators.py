import re
from typing import Any, Dict, Generator, Iterator, List

from src.utils import PATH_TO_JASON_FILE, get_transactions_from_json
from src.operations import PATH_TO_CSV_FILE, PATH_TO_EXCEL_FILE, get_operations_from_csv, get_operations_from_excel

transactions_json = get_transactions_from_json(PATH_TO_JASON_FILE)
transactions_csv = get_operations_from_csv(PATH_TO_CSV_FILE)
transactions_excel = get_operations_from_excel(PATH_TO_EXCEL_FILE)



def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator:
    """Функция возвращает итератор, который поочередно выдает транзакции с
    заданной валютой операции"""
    if not isinstance(transactions, list):
        return iter([]) # Если входные данные не список, возвращаем пустой итератор

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
    if not isinstance(transactions, list): # Если входные данные не являются списком, завершаем работу
        return

    for transaction in transactions:
        if not isinstance(transaction, dict): # Проверяем, что transaction — это словарь
            continue

        description = transaction.get("description", "")

        if isinstance(description, str) and description.strip(): # Проверяем, что описание — это строка и она не пустая
            yield description.strip()



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
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        yield []
