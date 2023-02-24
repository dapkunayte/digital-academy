from random import uniform
from itertools import chain


def create_random(n: int):  # Случайности не случайны
    for i in range(n):
        yield uniform(0, n)


print(list(create_random(3)))


def merge_list(list_1, list_2: list) -> list:  # Ленивое слияние
    return chain(list_1,list_2)


print(list(merge_list([1, 2], [3, 4])))


def responses_creator(item_ids):  # Рефакторинг
    if item_ids is None:
        item_ids = [None]
    responses = [dict(item_id=item_id) for item_id in item_ids]
    return responses


