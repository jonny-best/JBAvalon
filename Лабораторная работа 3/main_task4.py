salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

month = 10  # количество месяцев, которое можно прожить
while month > 0:  # TODO Оформить решение
    need_money = need_money + spend - salary
    spend += (spend * increase)
    month -= 1
print(round(need_money))

