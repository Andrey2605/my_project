def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты"""
    if card_number[-16:].isdigit() and len(card_number[-16:]) == 16:
        return (
            f"{card_number[:-16] }{card_number[-16:-12]} {card_number[-12:-10]}{"*" * 2} {"*" * 4} {card_number[-4:]}"
        )
    else:
        return "Не корректные данные"


def get_mask_account(mask_account: str) -> str:
    if mask_account[-20:].isdigit() and len(mask_account[-20:]) == 20:
        return f"{mask_account[:-20] }{"*" * 2}{mask_account[-4:]}"
    else:
        return "Не корректные данные"
