from typing import Dict, List, Union


def filter_by_state(
    list_operations: List[Dict[str, Union[str, int]]], state: str = "EXECUTED"
) -> List[Dict[str, Union[str, int]]]:
    """Отфильтровывает список словарей по заданному значению ключа state"""
    filtered_operations = []
    for operation in list_operations:
        if operation.get("state") == state:
            filtered_operations.append(operation)
    return filtered_operations


def sort_by_date(
    list_operations: List[Dict[str, Union[str, int]]], ascending: bool = True
) -> List[Dict[str, Union[str, int]]]:
    """Сортирует список словарей по дате, по умолчанию - убывание"""
    if ascending is True:
        sorted_operations = sorted(list_operations, key=lambda operation: operation.get("date"), reverse=True)
    elif ascending is False:
        sorted_operations = sorted(list_operations, key=lambda operation: operation.get("date"))
    return sorted_operations
