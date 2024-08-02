# import main


def get_mask_card_number(number_card: str) -> str:
    """Функцию маскировки номера банковской карты"""
    if number_card.isdigit() and len(number_card) == 16:
        return f"{number_card[:4]} {number_card[5:7]}{"*" * 2} {"*" * 4} {number_card[12:]}"
    else:
        return "Не корректные данные"


def get_mask_account(number_account: str) -> str:
    if number_account.isdigit() and len(number_account) == 20:
        return f"{"*" * 2} {number_account[16:]}"
    else:
        return "Не корректные данные"
