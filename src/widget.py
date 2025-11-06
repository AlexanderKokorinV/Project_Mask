import masks


def mask_account_card(type_number: str) -> str:
    """Принимает тип и номер карты или счета и возвращает замаскированный номер"""
    if type_number.startswith("Счет"):
        number = type_number[6:] #выделяем номер из строки
        mask_account = type_number[:5] + masks.get_mask_account(number)
    else:
        number = type_number[-16:] #выделяем номер из строки
        mask_account = type_number[:-16] + masks.get_mask_card_number(number)
    return mask_account


def get_date(date_string: str) -> str:
    """Принимает строку с датой и возвращает дату в заданном формате"""
    formatted_date = date_string[8:10] + "." + date_string[5:7] + "." + date_string[:4]
    return formatted_date