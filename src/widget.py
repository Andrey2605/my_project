from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user: str) -> str:
    """Функция для определения вводимых данных карты или счета"""
    if "Счет" in user:
        mask_account = user[-20:]
        return f"{user[:-20]}" + get_mask_account(mask_account)
    else:
        card_number = user[-16:]
        return f"{user[:-16]}" + get_mask_card_number(card_number)


def get_date(date: str) -> str:
    """Функцию преобразования даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
