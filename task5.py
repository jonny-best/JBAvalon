from string import ascii_letters, digits
from random import sample

def get_random_password(n) -> str:
    sample_ = sample(ascii_letters + digits, n)  # TODO написать функцию генерации случайных паролей
    return "".join(sample_)


print(get_random_password(8))
