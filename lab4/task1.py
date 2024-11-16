# TODO решите задачу
import json


def task() -> float:
    file_name = 'input.json'

    with open(file_name) as f:
        data = json.load(f)

    sum_of_values = sum(item['score'] * item['weight'] for item in data)
    return round(sum_of_values, 3)


print(task())
