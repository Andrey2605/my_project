from src.masks import get_mask_account, get_mask_card_number

number_card = input("Введите номер карты: ")
number_account = input("Введите номер счета: ")

print(get_mask_card_number(number_card))
print(get_mask_account(number_account))

# 1234567891234567
# 12345678912345678912
