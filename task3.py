import random

def get_unique_list_numbers() -> list[int]:
    list_=[]  # TODO написать функцию для получения списка уникальных целых чисел
    while len(list_) < 15:
        val = random.randint(-10, 10)
        if val not in list_:
            list_.append(val)

    return list_




list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))