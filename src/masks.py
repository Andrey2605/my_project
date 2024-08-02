def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[5:7]}{"*" * 2} {"*" * 4} {card_number[12:]}"
    else:
        return "Не корректные данные"


def get_mask_account(mask_account: str) -> str:
    if mask_account.isdigit() and len(mask_account) == 20:
        return f"{"*" * 2} {mask_account[16:]}"
    else:
        return "Не корректные данные"
