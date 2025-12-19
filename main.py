import os
import re
from typing import Dict, List, TypedDict, Union
from collections import deque, namedtuple, Counter
import json
import sys

from src.utils import PATH_TO_JASON_FILE, get_transactions_from_json
from src.operations import PATH_TO_CSV_FILE, PATH_TO_EXCEL_FILE, get_operations_from_csv, get_operations_from_excel
from src.decorators import log
from src.external_api import get_amount_in_rubles
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from src.search import search_transactions


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    final_transactions = [] # Создаем основную переменную, которая будет хранить текущее состояние списка

    # Блок 1. Выбор файла и загрузка данных
    while True:
        choose_option = input(
            """ 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
>
            """
        ).strip() # Убираем случайные пробелы при вводе
        if choose_option == "1":
            print("Для обработки выбран JSON-файл.")
            final_transactions = get_transactions_from_json(PATH_TO_JASON_FILE)
            break
        elif choose_option == "2":
            print("Для обработки выбран CSV-файл.")
            final_transactions = get_operations_from_csv(PATH_TO_CSV_FILE)
            break
        elif choose_option == "3":
            print("Для обработки выбран XLSX-файл.")
            final_transactions = get_operations_from_excel(PATH_TO_EXCEL_FILE)
            break
        else:
            print("Ошибка, неверный ввод. Пожалуйста, выберите 1, 2 или 3.\n>")

    if not final_transactions:
        print("Не удалось загрузить транзакции. Завершение программы.")
        return # Выход из программы, если данных нет

    # Блок 2. Фильтрация транзакций о статусу
    while True:
        state = str(input("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n>""")).strip().upper()
        if state in ["EXECUTED", "CANCELED", "PENDING"]:
            # Применяем фильтр к текущему списку и обновляем его
            final_transactions = filter_by_state(final_transactions, state)
            break
        else:
            print(f"Статус операции {state} недоступен.")
    # Блок 3. Сортировка транзакций по дате

    while True:
        sort_transactions_by_date = str(input("Отсортировать операции по дате? Да/Нет\n>")).strip().lower()
        if sort_transactions_by_date == "да":
            while True:
                sort_direction = str(input("Отсортировать по возрастанию или по убыванию? (введите: по возрастанию/по убыванию)\n>")).strip().lower()
                if sort_direction == "по возрастанию":
                    final_transactions = sort_by_date(final_transactions, ascending=False)
                    break
                elif sort_direction == "по убыванию":
                    final_transactions = sort_by_date(final_transactions, ascending=True)
                    break
                else:
                    print("Введено некорректное значение. Введите вариант сортировки: по возрастанию/по убыванию\n>")
            break # Выход из внешнего цикла "Да/Нет"
        elif sort_transactions_by_date == "нет":
            break # Выход из цикла "Да/Нет"
        else:
            print("Введено некорректное значение. Введите вариант: Да/Нет\n>")

    # Блок 4. Фильтрация транзакций по валюте (RUB)
    while True:
        get_ruble_transactions= str(input("Выводить только рублевые транзакции? Да/Нет\n>")).strip().lower()
        if get_ruble_transactions == "да":
            # Применяем фильтр к текущему списку и обновляем его
            final_transactions = list(filter_by_currency(final_transactions, currency="RUB"))
            break
        elif get_ruble_transactions == "нет":
            break
        else:
            print("Введено некорректное значение. Введите вариант: Да/Нет\n>")

    #Блок 5. Фильтрация по слову в описании транзакции
    while True:
        filter_by_category = str(input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n>")).strip().lower()
        if filter_by_category == "да":
            search = str(input(
                """
Введите слово для поиска. Возможные типы операций: 
'Перевод организации', 
'Перевод с карты на карту', 
'Перевод со счета на счет', 
'Открытие вклада'\n>
                """
            )).strip().lower()

            # Применяем фильтр к текущему списку и обновляем его
            final_transactions = search_transactions(final_transactions, search)
            break
        elif filter_by_category == "нет":
            break
        else:
            print("Введено некорректное значение. Введите вариант: Да/Нет\n>")

    # Итоговый вывод результата
    print("Распечатываю итоговый список транзакций...\n>")
    if not final_transactions:
        print("Не найдено ни одной транзакции, соответствующей заданным условиям")
    else:
        print(f"Всего найдено транзакций: {len(final_transactions)}")
        print(final_transactions)








if __name__ == "__main__":
    main()
