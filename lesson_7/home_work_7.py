"""
Задание 1. Безопасное деление
Напишите функцию safe_divide(a, b), которая:
Пытается вернуть a / b
Ловит ZeroDivisionError → возвращает 'Ошибка: деление на ноль'
Ловит TypeError (если переданы строки) → возвращает 'Ошибка: нужны числа'
"""


def save_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    except TypeError:
        return "Ошибка: нужны числа."


print(int(save_divide(8, 4)))
print(save_divide(5, 0))
print(save_divide(5, "f"))

"""
Задание 2. Безопасный поиск в словаре
Дан словарь config = {"host": "localhost", "port": 8080}.
Напишите функцию get_setting(key), которая:
Пытается вернуть config[key]
При KeyError возвращает "Настройка '{key}' не найдена"
Не используйте .get(), используйте именно try/except (для тренировки)
"""


def get_setting(key):
    try:
        config = {"host": "localhost", "port": 8080}
        return config[key]
    except KeyError:
        return f"Настройка '{key}' не найдена"


print(get_setting("host"))
print(get_setting("age"))

"""
Задание 3. Парсер числа с повтором
Напишите цикл while True, который запрашивает у пользователя год рождения через input().
Если введено не число → вывести "Введите цифры!" и запросить снова.
Если число < 1900 или > 2026 → вывести "Некорректный год" и запросить снова.
Если всё верно → вывести "Год принят: {year}" и выйти из цикла.
💡 Совет: В задании 3 используйте try: year = int(input(...)) except ValueError: ..., а проверку диапазона делайте через if.
"""


def get_valid_age():
    while True:
        try:
            birth_year = int(input("Введите свой год рождения: \n"))
            if birth_year < 1900 or birth_year > 2026:
                return "Некорректный год!"
                continue
            return f"Ваш год рождения: {birth_year}"
        except ValueError:
            return "Введите цифры!"


age = get_valid_age()

"""
✅ 4. Мини-тест
1. В каком порядке выполняются блоки: try, except, else, finally?
Ответ: выполняются в том порядке в каком и представлено в тесте

2. Почему except Exception: считается плохой практикой?
Ответ: потому что могут быть затерты разные ошибки, которые можно было исправить

3. Что произойдёт, если ошибка возникнет в блоке else? Будет ли она поймана except выше?
Ответ: возникнет новая ошибка вне блока try. Выше она не будет поймана.

4. Как получить текст ошибки внутри except для логирования?
Ответ: можно вывести функцией print
"""