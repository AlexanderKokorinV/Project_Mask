import os
from typing import Dict, List, TypedDict, Union

from src.decorators import log
from src.external_api import get_amount_in_rubles
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import get_transactions_from_json
from src.widget import get_date, mask_account_card
from src.operations import get_operations_from_csv, get_operations_from_excel


class Currency(TypedDict):
    name: str
    code: str


class OperationAmount(TypedDict):
    amount: str
    currency: Currency


class Transaction(TypedDict):
    id: int
    state: str
    date: str
    operationAmount: OperationAmount
    description: str
    from_: str
    to: str


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

transaction: Transaction = {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {"amount": "10000", "currency": {"name": "EUR", "code": "EUR"}},
    "description": "Перевод организации",
    "from_": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702",
}

if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(get_date("2024-03-11T02:26:18.671407"))
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            state="EXECUTED",
        )
    )

    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            ascending=True,
        )
    )

    usd_transactions = filter_by_currency(transactions, "RUB")
    for _ in range(2):
        print(next(usd_transactions, "Завершение итерации"))

    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
        print(next(descriptions, "Завершение итерации"))

    for card_number in card_number_generator(1, 5):
        print(card_number)

    @log(filename="mylog.txt")
    def apply_filter_by_state(
        list_operations: List[Dict[str, Union[str, int]]], state: str
    ) -> Union[List[Dict[str, Union[str, int]]], str]:
        return filter_by_state(list_operations, state)

    result_1 = apply_filter_by_state(
        [
            {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "CANCELED",
    )

    @log(filename="")
    def apply_get_mask_card_number(card_number: str) -> str:
        return get_mask_card_number(card_number)

    result_2 = apply_get_mask_card_number("70007922896063&1")

    PATH_TO_JASON_FILE = os.path.join(
        os.path.dirname(__file__), "data", "operations.json"
    )  # Формируем путь к файлу operations.json
    print(get_transactions_from_json(PATH_TO_JASON_FILE))

    print(get_amount_in_rubles(transaction))  # конвертируем сумму из евро в рубли

    PATH_TO_CSV_FILE = os.path.join(os.path.dirname(__file__), "data", "transactions.csv")
    print(get_operations_from_csv(PATH_TO_CSV_FILE))

    PATH_TO_EXCEL_FILE = os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")
    print(get_operations_from_excel(PATH_TO_EXCEL_FILE))
