def filter_by_state(list_operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Отфильтровывает список словарей по заданному значению ключа state"""
    filtered_operations = []
    for operation in list_operations:
        if operation.get("state") == state:
            filtered_operations.append(operation)
    return filtered_operations
