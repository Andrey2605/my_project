# from src.widget import get_date, mask_account_card
#
# user = input("Введите номер карты или номер счета: ")
# date = input("Введите дату: ")
#
# print(mask_account_card(user))
# print(get_date(date))

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.search_by_world import filter_by_world
from src.tables import get_transactions_csv, get_transactions_excel
from src.utils import read_file
from src.widget import get_date, mask_account_card


def main() -> None:
    """Выбор файла для открытия"""
    global reverse
    while True:
        print(
            """Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
        )
        user = input()

        if user == "1":
            transact = read_file("../my_project/data/operations.json")
            break
        elif user == "2":
            transact = get_transactions_csv("../my_project/data/transactions.csv")
            break
        elif user == "3":
            transact = get_transactions_excel("../my_project/data/transactions_excel.xlsx")
            break
        else:
            print("Не корректные данные, попробуйте еще раз.")

    filter_transaction = transact

    """Выбор статуса для фильтрации"""

    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        user = str(input()).upper()

        if user in ["EXECUTED", "CANCELED", "PENDING"]:
            filter_transaction = filter_by_state(user, transact)
            break
        else:
            print(f"Статус операции {user} недоступен.")

    print(f"Операции отфильтрованы по статусу {user}")

    print("Отсортировать операции по дате? Да/Нет")
    user = str(input()).title()
    if user == "Да":
        print("Отсортировать по возрастанию или по убыванию?")
        user = input()
        if user == "по возрастанию":
            reverse = False
        elif user == "по убыванию":
            reverse = True
        filter_transaction = sort_by_date(filter_transaction, reverse)

    print("Выводить только рублевые тразакции? Да/Нет")
    user = str(input()).title()
    if user == "Да":
        filter_transaction = list(filter_by_currency(filter_transaction, "RUB"))
    elif user == "Нет":
        filter_transaction = filter_transaction

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user = str(input()).title()
    if user == "Да":
        print("Введите слово: ")
        world = input()
        filter_transaction = filter_by_world(filter_transaction, world)

    print("Распечатываю итоговый список транзакций...")

    if len(filter_transaction) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filter_transaction)}")
        for transaction in filter_transaction:
            transaction_date = get_date(transaction["date"])
            if "operationAmount" in transaction:
                currency = transaction["operationAmount"]["currency"]["code"]
            else:
                currency = transaction["currency_code"]
            if transaction["description"] == "Открытие вклада":
                from_to = mask_account_card(transaction["to"])
            else:
                from_to = mask_account_card(transaction["from"]) + " -> " + mask_account_card(transaction["to"])

            if "amount" in transaction:
                amount = transaction["amount"]
            elif "operationAmount" in transaction:
                amount = transaction["operationAmount"]["amount"]
            print(
                f"""{transaction_date} {transaction['description']}
{from_to}
Сумма: {round(float(amount))} {currency}"""
            )


if __name__ == "__main__":
    main()
