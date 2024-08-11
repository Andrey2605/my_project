date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

state = "EXECUTED"


def filter_by_state(state: str) -> list:
    """Функция возвращает новый список словарей, у которых ключ state соответствует указанному значению"""
    new_list = []
    for dictonary in date:
        if dictonary["state"] == state:
            new_list.append(dictonary)
    return new_list


print(filter_by_state(state))


def sort_by_date(date: list) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    sorted_list = sorted(date, key=lambda x: x["date"], reverse=True)
    return sorted_list


print(sort_by_date(date))
