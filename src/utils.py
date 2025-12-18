import json
import logging
import os
from typing import Any


PATH_TO_LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "utils.log")
utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(PATH_TO_LOG_FILE, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)


utils_logger.info("Формируем путь к файлу operations.json")
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))  # Определяем путь к корневой папке проекта
PATH_TO_JASON_FILE = os.path.join(ROOT_DIR, "data", "operations.json")  # Формируем путь к файлу operations.json


def get_transactions_from_json(PATH_TO_JASON_FILE: str) -> Any:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список
    """
    try:
        utils_logger.info(
            "Принимаем путь к файлу operations.json и возвращаем список словарей с данными о финансовых транзакциях"
        )
        with open(PATH_TO_JASON_FILE, encoding="utf-8") as file:
            list_transactions = json.load(file)
            return list_transactions
    except FileNotFoundError:
        utils_logger.error("Ошибка: файл не найден")
        return []
    except ValueError:
        utils_logger.error("Ошибка: файл пуст, либо содержит не список")
        return []
    except json.JSONDecodeError:
        utils_logger.error("Ошибка: файл содержит некорректные данные")
        return []
