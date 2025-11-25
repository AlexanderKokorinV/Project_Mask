import json
import os
from typing import Any

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))  # Определяем путь к корневой папке проекта
PATH_TO_JASON_FILE = os.path.join(ROOT_DIR, "data", "operations.json")  # Формируем путь к файлу operations.json


def get_transactions_from_json(PATH_TO_JASON_FILE: str) -> Any:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список
    """
    try:
        with open(PATH_TO_JASON_FILE, encoding="utf-8") as file:
            list_transactions = json.load(file)
            return list_transactions
    except FileNotFoundError:
        return []
    except ValueError:
        return []
    except json.JSONDecodeError:
        return []
