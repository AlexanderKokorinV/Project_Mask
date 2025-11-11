def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает его замаскированную версию"""
    if card_number.isdigit() and len(card_number) == 16:
        mask_number = card_number[:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[-4:]
    else:
        mask_number = "Ошибка"
    return mask_number


def get_mask_account(account: str) -> str:
    """Принимает на вход номер банковского счета и возвращает его замаскированную версию"""
    if account.isdigit() and len(account) == 20:
        mask_account = "**" + account[-4:]
    else:
        mask_account = "Ошибка"
    return mask_account
