import re
from typing import Dict, List


def search_transactions(transactions: List[Dict], search: str) -> List[Dict]:
    """Отфильтровывает список транзакций по заданному слову в описании (description)"""
    search_query = str(search).strip()  # Убираем лишние пробелы из запроса
    if not search_query:
        return []

    filtered_transactions = []
    for transaction in transactions:
        description = transaction.get("description", "")
        if isinstance(description, str):
            description = description.strip()
            if description and re.search(search_query, description, flags=re.IGNORECASE):
                filtered_transactions.append(transaction)

    return filtered_transactions
