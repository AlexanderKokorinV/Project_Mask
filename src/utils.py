import json
import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__)) # Определяем путь к корневой папке проекта
PATH_TO_JASON_FILE = os.path.join(ROOT_DIR, "data", "operations.json") # Формируем путь к файлу operations.json

def get_transactions_from_json(PATH_TO_JASON_FILE):
    try:
        with open(PATH_TO_JASON_FILE, encoding='utf-8') as f:
            list_transactions = json.load(f)
            return list_transactions
    except FileNotFoundError:
            return []
    except ValueError:
            return []
    except json.JSONDecodeError:
            return []

print(get_transactions_from_json(PATH_TO_JASON_FILE))