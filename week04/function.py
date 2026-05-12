# 1. вызов функции
def say_hello():
    print("Привет! Я функция.")


say_hello()
say_hello()
print("-" * 15)


# 2. Функция с аргументами
def greet(name, age):
    print(f"Привет, {name}! Тебе {age} лет.")


greet("Анна", 21)
greet("Виктор", 50)
print("-" * 15)


# 3. return vs print
def add_numbers(a, b):
    result = a + b
    return result  # отдаем число, а не просто показываем


# Используем результат дальше
sum_val = add_numbers(5, 3)
print(sum_val * 2)
print("-" * 15)


# 4. Значение по умолчанию
def make_coffee(size="medium", sugar=True):
    print(f"Готовим кофе: {size}, сахар: {sugar}")


make_coffee()
make_coffee("large")
make_coffee(sugar=False)
print("-" * 15)
