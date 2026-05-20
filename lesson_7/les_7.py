# 1. БАЗОВАЯ ЗАЩИТА
try:
    number = int(input("Введите число: "))
    result = 10 / number
    print(f"Результат: {result}")
except ValueError:
    print("Это не число! Пожалуйста введите цифры.")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except Exception as e:
    print(f"Неожиданная ошибка {e}")

# 2. TRY / EXCEPT / ELSE / FINALLY
try:
    data = {"key": "value"}
    result = data["missing_key"] # Вызовет KeyError
except KeyError:
    print("Ключ не найден")
else:
    print("Все прошло гладко") # Сработает, только если нет ошибок
finally:
    print("Завершающая очистка (выполняется всегда")

# 3. ПОЛЕЗНЫЙ ПАТЕРН: повторный запрос при ошибке
def get_valid_age():
    while True:
        try:
            age = int(input("Введите свой возраст: "))
            if age < 0:
                print("Возраст не может быть отрицательным!")
                continue
            print(f"Вам {age} лет.")  # выводим печать в консоль
            #return age               # возвращаем значение
        except ValueError:
            print("Пожалуйста, введите целое число.")


age = get_valid_age()
