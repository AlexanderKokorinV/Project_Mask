import os
import re
from typing import Dict, List, TypedDict, Union
from collections import deque, namedtuple, Counter
import json


from src.decorators import log
from src.external_api import get_amount_in_rubles
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.operations import get_operations_from_csv, get_operations_from_excel
from src.processing import filter_by_state, sort_by_date
from src.utils import get_transactions_from_json
from src.widget import get_date, mask_account_card


def main():
    while True:
        choose_option = input(
            """ 
            Привет! Добро пожаловать в программу работы с банковскими транзакциями.
            
            Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла\n>
            """
        )
        if choose_option == "1":
            print("Для обработки выбран JSON-файл.")

        elif choose_option == "2":
            print("Для обработки выбран CSV-файл.")
        elif choose_option == "3":
            print("Для обработки выбран XLSX-файл.")
        else:
            print("Ошибка, неверный ввод. Пожалуйста, выберите 1, 2 или 3.")


if __name__ == "__main__":
    main()
