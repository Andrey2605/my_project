import re
from collections import Counter


def filter_by_world(filtered_transactions: list[dict], world: str) -> list[dict]:
    new_list = []
    for operation in filtered_transactions:
        if re.search(world, operation.get("description", "")):
            new_list.append(operation)
            filtered_transactions = new_list
    return filtered_transactions


def count_by_category(transactions: list[dict], category: list[str]) -> dict:
    count_by_category = []
    for transaction in transactions:
        if "description" in transaction and transaction["description"] in category:
            count_by_category.append(transaction["decripton"])
    count = Counter(count_by_category)
    return count
