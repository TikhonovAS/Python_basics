# Задача: Написать функцию, которая принимает сумму в рублях и курс доллара
# Возвращает сумму в долларах
# Пример вызова: print(usd_from_rub(1000, 90)

def usd_from_rub(rub_amount, exchange_rate):
    result = rub_amount / exchange_rate
    return result

print(usd_from_rub(1000, 90))