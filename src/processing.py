from typing import Dict, List, Union
from src.utils import PATH_TO_JASON_FILE, get_transactions_from_json
from src.operations import PATH_TO_CSV_FILE, PATH_TO_EXCEL_FILE, get_operations_from_csv, get_operations_from_excel

transactions_json = get_transactions_from_json(PATH_TO_JASON_FILE)
transactions_csv = get_operations_from_csv(PATH_TO_CSV_FILE)
transactions_excel = get_operations_from_excel(PATH_TO_EXCEL_FILE)


def filter_by_state(
    transactions: List[Dict], state: str
) -> List[Dict]:
    """Отфильтровывает список словарей по заданному значению ключа state"""
    if not isinstance(transactions, list):
        return []

    filtered_transactions = []
    for transaction in transactions:
        if isinstance(transaction, dict) and transaction.get("state", "Ошибка") == state:
            filtered_transactions.append(transaction)

    return filtered_transactions


def sort_by_date(
    transactions: List[Dict], ascending: bool = True
) -> List[Dict]:
    """Сортирует список словарей по дате, по умолчанию - убывание"""
    if not isinstance(transactions, list):
        return []
    try:
        if ascending is True:
            sorted_transactions = sorted(
                transactions,
                key=lambda transaction: transaction.get("date","Ошибка"),
                reverse=True,
            )
        elif ascending is False:
            sorted_transactions = sorted(
                transactions,
                key=lambda transaction: transaction.get("date", "Ошибка")
            )
    except TypeError:
        return "Ошибка"
    except ValueError:
        return "Ошибка"
    return sorted_transactions
