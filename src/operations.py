import os
from typing import Any

import pandas as pd

PATH_TO_CSV_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
PATH_TO_EXCEL_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def get_operations_from_csv(PATH_TO_CSV_FILE: str) -> Any:
    """Принимаем путь к CSV-файлу и возвращаем список словарей с транзакциями"""
    try:
        df_from_csv = pd.read_csv(PATH_TO_CSV_FILE, encoding="utf-8", delimiter=";")
        list_transactions_csv = df_from_csv.to_dict(orient="records")
        return list_transactions_csv
    except FileNotFoundError:
        # Обработка случая, если файл по указанному пути не найден
        return []
    except ValueError:
        # Обработка случая, если файл пуст, либо содержит некорректные данные
        return []
    except Exception:
        # Обработка любых других непредвиденных ошибок при чтении
        return []


def get_operations_from_excel(PATH_TO_EXCEL_FILE: str) -> Any:
    """Принимаем путь к excel-файлу и возвращаем список словарей с транзакциями"""
    try:
        df_from_excel = pd.read_excel(PATH_TO_EXCEL_FILE)
        list_transactions_excel = df_from_excel.to_dict(orient="records")
        return list_transactions_excel
    except FileNotFoundError:
        # Обработка случая, если файл по указанному пути не найден
        return []
    except ValueError:
        # Обработка случая, если файл пуст, либо содержит некорректные данные
        return []
    except Exception:
        # Обработка любых других непредвиденных ошибок при чтении
        return []
