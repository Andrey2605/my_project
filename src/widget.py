from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user: str) -> str:
    """Функция для определения вводимых данных карты или счета"""
    if "Счет" in user:
        mask_account = user
        return get_mask_account(mask_account)
    else:
        card_number = user
        return get_mask_card_number(card_number)


def get_date(date: str) -> str:
    """Функцию преобразования даты"""
    if len(date) == 26 and date[4:8:3] == "--":
        return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    else:
        return "Не корректные данные"

