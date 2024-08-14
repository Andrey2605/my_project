from src.widget import get_date, mask_account_card


user = input("Введите номер карты или номер счета: ")
date = input("Введите дату: ")

print(mask_account_card(user))
print(get_date(date))

