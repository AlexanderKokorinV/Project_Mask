from typing import Dict, List, Union


def filter_by_state(
    list_operations: List[Dict[str, Union[str, int]]], state: str = "EXECUTED"
) -> Union[List[Dict[str, Union[str, int]]], str]:
    """Отфильтровывает список словарей по заданному значению ключа state"""
    try:
        filtered_operations = []
        for operation in list_operations:
            if "state" in operation and "id" in operation and "date" in operation:
                if operation.get("state") == state:
                    filtered_operations.append(operation)
                elif operation.get("state") not in ["EXECUTED", "CANCELED"]:
                    raise ValueError("Ошибка")
            else:
                raise ValueError("Ошибка")
    except ValueError:
        return "Ошибка"
    return filtered_operations


def sort_by_date(
    list_operations: List[Dict[str, Union[str, int]]], ascending: bool = True
) -> Union[List[Dict[str, Union[str, int]]], str]:
    """Сортирует список словарей по дате, по умолчанию - убывание"""
    try:
        sorted_operations = []
        for operation in list_operations:
            if len(list_operations) > 0 and "date" in operation:
                if ascending is True:
                    sorted_operations = sorted(
                        list_operations, key=lambda operation: operation.get("date", "Ошибка"), reverse=True
                    )
                elif ascending is False:
                    sorted_operations = sorted(list_operations, key=lambda operation: operation.get("date", "Ошибка"))
            else:
                raise ValueError("Ошибка")
                break
    except ValueError:
        return "Ошибка"
    except TypeError:
        return "Ошибка"
    return sorted_operations
