import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/masks.log')
file_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты"""
    logger.info('Выполнение маскировки карты')
    if card_number[-16:].isdigit() and len(card_number[-16:]) == 16:
        return (
            f"{card_number[:-16]}{card_number[-16:-12]} {card_number[-12:-10]}{"*" * 2} {"*" * 4} {card_number[-4:]}"
        )
    else:
        logging.warning('Введены не корректные данные')
        return "Не корректные данные"


def get_mask_account(mask_account: str) -> str:
    logging.info('Выполнение маскировки счета')
    if mask_account[-20:].isdigit() and len(mask_account[-20:]) == 20:
        return f"{mask_account[:-20]}{"*" * 2}{mask_account[-4:]}"
    else:
        logging.warning('Введены не корректные данные')
        return "Не корректные данные"
