from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user: str) -> str:
    if "Счет" in user:
        mask_account = user[-20:]
        return get_mask_account(mask_account)
    else:
        card_number = user[-16:]
        return get_mask_card_number(card_number)
