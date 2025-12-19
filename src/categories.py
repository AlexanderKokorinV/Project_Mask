from collections import Counter

from src.utils import PATH_TO_JASON_FILE, get_transactions_from_json
from src.operations import PATH_TO_CSV_FILE, PATH_TO_EXCEL_FILE, get_operations_from_csv, get_operations_from_excel
from typing import List, Dict

transactions_json = get_transactions_from_json(PATH_TO_JASON_FILE)
transactions_csv = get_operations_from_csv(PATH_TO_CSV_FILE)
transactions_excel = get_operations_from_excel(PATH_TO_EXCEL_FILE)

def count_categories(transactions: List[Dict], descriptions: List) -> Dict[str, int]:
    """Подсчет количества банковских операций определенного типа (поле description)"""
    if not isinstance(transactions, list):
        return {}

    count_by_category = Counter(transaction.get("description", "") for transaction in transactions if transaction.get("description", "") in descriptions)
    return dict(count_by_category)
