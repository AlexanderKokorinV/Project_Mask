import re
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_number: str) -> str:
    """Принимает тип и номер карты или счета и возвращает замаскированный номер"""
    if type_number.startswith("Счет"):
        if len(type_number) == 25:
            number = type_number[5:]  # выделяем номер из строки
            mask_account = type_number[:5] + get_mask_account(number)
        else:
            mask_account = "Ошибка"
    else:
        if re.fullmatch(r"[а-яА-Яa-zA-Z \s-]+", type_number[:-16]):
            number = type_number[-16:]  # выделяем номер из строки
            mask_account = type_number[:-16] + get_mask_card_number(number)
        else:
            mask_account = "Ошибка"
    return mask_account


def get_date(date_string: str) -> str:
    """Принимает строку с датой и возвращает дату в заданном формате"""
    if date_string[8:10].isdigit() and date_string[5:7].isdigit() and date_string[:4].isdigit() and len(date_string) == 26:
        formatted_date = date_string[8:10] + "." + date_string[5:7] + "." + date_string[:4]
    else:
        formatted_date = "Ошибка"
    return formatted_date
