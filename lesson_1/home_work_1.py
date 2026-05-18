"""
Задание 1. Профиль пользователя
Создайте 4 переменные: username (строка), user_age (целое число), balance (дробное число), is_premium (логическое).
Выведите тип каждой с помощью type().
"""
username = "admin"
user_age = 25
balance = 1000.0
is_premium = True

print(type(username))
print(type(user_age))
print(type(balance))
print(type(is_premium))


"""Задание 2. Исправьте ошибку
score = 95
print("Ваш результат: " + score)"""

score = 95
print("Ваш результат: " + str(score)) # 1 вариант
print(f"Ваш результат: {score}")      # 2 вариант

"""
Задание 3. Калькулятор ИМТ (индекс массы тела)
Формула: ИМТ = вес / (рост * рост)
Создайте переменные weight = 70 и height_m = 1.75. Посчитайте ИМТ, сохраните в переменную bmi и выведите сообщение:
"Ваш ИМТ: 22.86" (округлять не обязательно, Python покажет дробь).
"""
weight = 70
height = 1.75

bmi = round(weight /(height * height), 2)

print(f"Ваш ИМТ: {bmi}")