import logging

masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает его замаскированную версию"""
    if card_number.isdigit() and len(card_number) == 16:
        mask_number = card_number[:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[-4:]
        masks_logger.info(
            f"Принимаем на вход номер карты {card_number} и возвращаем его в замаскированном виде {mask_number}"
        )
    else:
        masks_logger.error("Ошибка: некорректный формат номера карты")
        mask_number = "Ошибка"
    return mask_number


def get_mask_account(account: str) -> str:
    """Принимает на вход номер банковского счета и возвращает его замаскированную версию"""
    if account.isdigit() and len(account) == 20:
        mask_account = "**" + account[-4:]
        masks_logger.info(
            f"Принимаем на вход номер банковского счета {account} и возвращаем в замаскированном виде {mask_account}"
        )
    else:
        masks_logger.error("Ошибка: некорректный формат номера банковского счета")
        mask_account = "Ошибка"
    return mask_account
