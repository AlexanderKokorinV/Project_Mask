import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(operation_data: list[dict]) -> None:
    """Тест работы функции в обычном режиме"""
    assert filter_by_state(operation_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.parametrize(
    "operation_data, status, expected",
    [
        ({"id": 939719570, "date": "2018-06-30T02:08:58.425572"}, "EXECUTED", "Ошибка"),
        ({"state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}, "EXECUTED", "Ошибка"),
        ({"id": 939719570, "state": "EXECUTED"}, "EXECUTED", "Ошибка"),
        ({""}, "EXECUTED", "Ошибка"),
        ({"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"}, "", "Ошибка"),
        ({"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"}, "67253", "Ошибка"),
    ],
)
def test_filter_by_state_par(operation_data: list[dict], status: str, expected: str) -> None:
    """Тест работы функции при различных параметрах, вызывающих ошибку"""
    assert filter_by_state(operation_data) == expected


def test_sort_by_date_default(operation_data: list[dict]) -> None:
    """Тест работы функции в обычном режиме, сортировка по умолчанию - убывание"""
    assert sort_by_date(operation_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_ascending(operation_data: list[dict], ascending: bool = False) -> None:
    """Тест работы функции в обычном режиме, сортировка по возрастанию"""
    assert sort_by_date(operation_data, ascending=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date(operation_data_same_date: list[dict], ascending: bool = False) -> None:
    """Тест работы функции в обычном режиме, сортировка при одинаковых датах"""
    assert sort_by_date(operation_data_same_date, ascending=True) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.mark.parametrize(
    "operation_list, ascending, expected",
    [
        ({"id": 41428829, "state": "EXECUTED", "date": "-07-03T18:35:29.512364"}, True, "Ошибка"),
        ({"id": 939719570, "state": "EXECUTED", "date": "2018-06-T02:08:58.425572"}, True, "Ошибка"),
        ({"id": 594226727, "state": "CANCELED", "date": "2018-09-12T787878721:27:25.241689"}, True, "Ошибка"),
        ({"id": 939719570, "state": "EXECUTED", "date": "2018/06/30T02:08:58.425572"}, True, "Ошибка"),
        ({"id": 939719570, "state": "EXECUTED", "date": "2018.06.30T02:08:58.425572"}, True, "Ошибка"),
        ({"id": 615064591, "state": "CANCELED", "date": "201"}, True, "Ошибка"),
        ({"id": 615064591, "state": "CANCELED"}, True, "Ошибка"),
    ],
)
def test_sort_by_date_par(operation_list: list[dict], ascending: bool, expected: str) -> None:
    """Тест работы функции при различных параметрах, вызывающих ошибку"""
    assert sort_by_date(operation_list, ascending) == expected
