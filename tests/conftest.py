from typing import Dict, List, TypedDict, Union

import pytest


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


@pytest.fixture
def card_numbers() -> str:
    return "7000792289606361"


@pytest.fixture
def account_numbers() -> str:
    return "73654108430135874305"


@pytest.fixture
def card() -> str:
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def account() -> str:
    return "Счет 73654108430135874305"


@pytest.fixture
def date_str() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def operation_data() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def operation_data_same_date() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def operation_status() -> str:
    return "EXECUTED"


@pytest.fixture
def transactions() -> list[dict]:
    return [
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


@pytest.fixture
def start() -> int:
    return 1


@pytest.fixture
def stop() -> int:
    return 5


@pytest.fixture
def transaction_rub() -> Transaction:
    return {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод с карты на счет",
        "from_": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612",
    }


@pytest.fixture
def mock_source_data() -> Dict[str, List[Union[int, float, str]]]:
    """Фикстура, предоставляющая исходные данные для mock DataFrame."""
    return {  # Создаем фиктивный DataFrame, который будет "возвращать" mock_read_csv/mock_read_excel
        "id": [1245327.0, 134341.0],
        "state": ["PENDING", "CANCELED"],
        "date": ["2021-03-09T00:56:48Z", "2022-03-03T08:41:08Z"],
        "amount": [24252.0, 13642.0],
        "currency_name": ["Somoni", "Peso"],
        "currency_code": ["TJS", "COP"],
        "from": ["Discover 3233958335206913", "Visa 9770850749183268"],
        "to": ["Visa 6269545625045856", "American Express 0522499169905654"],
        "description": ["Перевод с карты на карту", "Перевод с карты на карту"],
    }


@pytest.fixture
def expected_list_of_dicts() -> List[Dict[str, Union[int, float, str]]]:
    """Фикстура, предоставляющая ожидаемый итоговый результат."""
    return [  # Ожидаемый результат в формате списка словарей
        {
            "id": 1245327.0,
            "state": "PENDING",
            "date": "2021-03-09T00:56:48Z",
            "amount": 24252.0,
            "currency_name": "Somoni",
            "currency_code": "TJS",
            "from": "Discover 3233958335206913",
            "to": "Visa 6269545625045856",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 134341.0,
            "state": "CANCELED",
            "date": "2022-03-03T08:41:08Z",
            "amount": 13642.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Visa 9770850749183268",
            "to": "American Express 0522499169905654",
            "description": "Перевод с карты на карту",
        },
    ]


@pytest.fixture
def mock_csv_file_path() -> str:
    """Фикстура, предоставляющая фиктивный путь к CSV-файлу."""
    return "fake/path/to/transactions.csv"


@pytest.fixture
def mock_excel_file_path() -> str:
    """Фикстура, предоставляющая фиктивный путь к excel-файлу."""
    return "fake/path/to/transactions_excel.xlsx"
