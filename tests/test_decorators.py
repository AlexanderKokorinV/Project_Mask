from typing import Any


def test_log_fail(capsys: Any) -> None:
    """Тест вывода в консоль при обработке исключения"""

    from src.decorators import log
    from src.masks import get_mask_card_number

    @log(filename="")
    def apply_get_mask_card_number(card_number: str) -> str:
        """Функция принимает аргумент (строку с номером банковской карты)
        и возвращает результат выполнения функции get_mask_card_number из модуля masks"""
        return get_mask_card_number(card_number)

    apply_get_mask_card_number("7000792289606&8")
    captured = capsys.readouterr()
    assert "ValueError" in captured.out


def test_log_success(capsys: Any) -> None:
    """Тест вывода в консоль при успешном выполнении функции"""

    from src.decorators import log
    from src.masks import get_mask_card_number

    @log(filename="")
    def apply_get_mask_card_number(card_number: str) -> str:
        """Функция принимает аргумент (строку с номером банковской карты)
        и возвращает результат выполнения функции get_mask_card_number из модуля masks"""
        return get_mask_card_number(card_number)

    apply_get_mask_card_number("7000792289606361")
    captured = capsys.readouterr()
    assert "apply_get_mask_card_number ok" in captured.out


def test_log_in_file_err() -> None:
    """Тест вывода в лог-файл my_log.txt при обработке исключения"""

    from src.decorators import log
    from src.masks import get_mask_card_number

    @log(filename="mylog.txt")
    def apply_get_mask_card_number(card_number: str) -> str:
        """Функция принимает аргумент (строку с номером банковской карты)
        и возвращает результат выполнения функции get_mask_card_number из модуля masks"""
        return get_mask_card_number(card_number)

    apply_get_mask_card_number("700079228960^&@1")
    with open("mylog.txt") as file:
        assert "ValueError" in file.read()


def test_log_in_file_suc() -> None:
    """Тест вывода в лог-файл my_log.txt при успешном выполнении"""

    from src.decorators import log
    from src.masks import get_mask_card_number

    @log(filename="mylog.txt")
    def apply_get_mask_card_number(card_number: str) -> str:
        """Функция принимает аргумент (строку с номером банковской карты)
        и возвращает результат выполнения функции get_mask_card_number из модуля masks"""
        return get_mask_card_number(card_number)

    apply_get_mask_card_number("7000792289606361")
    with open("mylog.txt") as file:
        assert "apply_get_mask_card_number ok" in file.read()
