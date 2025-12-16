import csv
import pandas as pd
import os

PATH_TO_CSV_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")

def get_operations_from_csv(PATH_TO_CSV_FILE):
    """Принимаем путь к CSV-файлу и возвращаем список словарей с транзакциями"""
    try:
        df_from_csv = pd.read_csv(PATH_TO_CSV_FILE, delimiter=";")
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


print(get_operations_from_csv(PATH_TO_CSV_FILE))
