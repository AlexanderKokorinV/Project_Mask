def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает его замаскированную версию"""
    mask_number = card_number[:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[-4:]
    return mask_number


def get_mask_account(account: str) -> str:
    """Принимает на вход номер банковского счета и возвращает его замаскированную версию"""
    mask_account = "**" + account[-4:]
    return mask_account

