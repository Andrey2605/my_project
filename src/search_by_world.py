import re


def filter_by_world(filtered_transactions: list[dict], world: str) -> list[dict]:
    new_list = []
    for operation in filtered_transactions:
        if re.search(world, operation.get("description", "")):
            new_list.append(operation)
            filtered_transactions = new_list
    return filtered_transactions

