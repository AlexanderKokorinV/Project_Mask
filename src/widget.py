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

