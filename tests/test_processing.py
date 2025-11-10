import pytest
from src.processing import filter_by_state

def test_filter_by_state(operation_data):
    """Тест работы функции в обычном режиме"""
    assert filter_by_state(operation_data) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", 'date': "2018-09-12T21:27:25.241689"}
    ]

@pytest.mark.parametrize("list_operations, status, expected", [
    ({"id": 939719570, "date": "2018-06-30T02:08:58.425572"},"EXECUTED", "Ошибка"),
    ({"state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},"EXECUTED", "Ошибка"),
    ({"id": 939719570, "state": "EXECUTED"},"EXECUTED", "Ошибка"),
    ({""},"EXECUTED", "Ошибка"),
    ({"id": 594226727, "state": "EXECUTED", 'date': "2018-09-12T21:27:25.241689"}, "", "Ошибка"),
    ({"id": 594226727, "state": "EXECUTED", 'date': "2018-09-12T21:27:25.241689"}, "67253", "Ошибка")
]
                         )
def test_filter_by_state_par(list_operations, status, expected):
    assert filter_by_state(list_operations) == expected

