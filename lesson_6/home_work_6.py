"""
Задание 1. Функция приветствия
Напишите функцию greet_user(name, is_premium=False), которая:
Если is_premium=True → возвращает 'Добро пожаловать, {name}! '
Иначе → возвращает 'Привет, {name}!'
"""


def greet_user(name, is_premium=False):
    if is_premium == True:
        return f"Добро пожаловать, {name}!"
    else:
        return f"Привет, {name}!"


name_1 = print(greet_user("Виктор"))
name_2 = print(greet_user("Александр", is_premium=True))

"""
Задание 2. Валидатор пароля
Функция is_valid_password(password) проверяет:
Длина ≥ 8 символов
Содержит хотя бы одну цифру (подсказка: any(char.isdigit() for char in password))
Не содержит пробелов
Возвращает True, если всё верно, иначе False.
"""


def is_valid_password(password):
    if len(password) >= 8 and any(char.isdigit() for char in password) and not " " in password:
        return True
    else:
        return False


result = print(is_valid_password("HTYJkjufyC759VE"))
"""
Задание 3. Конвертер валют (с кэшем)
Функция convert_currency(amount, from_curr, to_curr, rates) где:
rates — словарь курсов: {"USD": 90, "EUR": 100} (относительно рубля)
Конвертирует: amount * rates[to_curr] / rates[from_curr]
Возвращает результат, округлённый до 2 знаков
Пример: convert_currency(100, "USD", "EUR", {"USD": 90, "EUR": 100}) → 90.0
"""


def convert_currency(amount, from_curr, to_curr, rates):
    result = amount * rates[to_curr] / rates[from_curr]
    return round(result, 2)


print(convert_currency(100, "USD", "EUR", {"USD": 90, "EUR": 100}))

"""✅ 4. Мини-тест
1. Что вернёт функция без return?
Ответ: None
2. В чём разница между print() внутри функции и return?
Ответ: print() - выводит, то что в скобках в консоль, а return возвращает значения
3. Можно ли переопределить функцию, объявив её дважды с тем же именем?
Ответ: Вопрос немного не понятен, Если вызвать дважды функцию, то она выполнит 2 раза свою работу, а переопределить можно исправив тело самой функции
4. Что такое «побочный эффект» функции? Приведите пример.
Ответ: Побочный эффект, я так понимаю, речь про вывод текста в консоль? Типа: print("Hello!")
"""
