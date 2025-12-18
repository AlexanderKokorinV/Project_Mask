import re

from utils import PATH_TO_JASON_FILE, get_transactions_from_json
from operations import PATH_TO_CSV_FILE, PATH_TO_EXCEL_FILE, get_operations_from_csv, get_operations_from_excel
from typing import List, Dict

transactions_json = get_transactions_from_json(PATH_TO_JASON_FILE)
transactions_csv = get_operations_from_csv(PATH_TO_CSV_FILE)
transactions_excel = get_operations_from_excel(PATH_TO_EXCEL_FILE)

def search_transactions_from_json(transactions_json: List[Dict], search: str) -> List[Dict]:
    """Отфильтровывает список транзакций из JSON-файла по заданному слову в описании (description)"""
    search_query = str(search).strip() #Убираем лишние пробелы из запроса
    filtered_transactions = []
    for transaction in transactions_json:
        description = str(transaction.get("description")).strip() #Извлекаем описание, убираем лишние пробелы
        if description and re.search(search_query, description, flags=re.IGNORECASE):
            filtered_transactions.append(transaction)
    return filtered_transactions


def search_transactions_from_csv(transactions_csv: List[Dict], search: str) -> List[Dict]:
    """Отфильтровывает список транзакций из CSV-файла по заданному слову в описании (description)"""
    search_query = str(search).strip() #Убираем лишние пробелы из запроса
    filtered_transactions = []
    for transaction in transactions_csv:
        description = str(transaction.get("description")).strip() #Извлекаем описание, убираем лишние пробелы
        if description and re.search(search_query, description, flags=re.IGNORECASE):
            filtered_transactions.append(transaction)
    return filtered_transactions


def search_operations_from_excel(operations_json: List[Dict], search: str) -> List[Dict]:
    """Отфильтровывает список транзакций из XLSX-файла по заданному слову в описании (description)"""
    search_query = str(search).strip() #Убираем лишние пробелы из запроса
    filtered_transactions = []
    for transaction in transactions_excel:
        description = str(transaction.get("description")).strip() #Извлекаем описание, убираем лишние пробелы
        if description and re.search(search_query, description, flags=re.IGNORECASE):
            filtered_transactions.append(transaction)
    return filtered_transactions












