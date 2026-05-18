# 1️⃣ СОЗДАНИЕ ПЕРЕМЕННЫХ
age = 25                # int: целое число
height = 1.78           # float: дробное число
name = "Мария"          # str: строка (в кавычках!)
is_active = True        # bool: логическое значение
secret = None           # None: пока ничего, но место готово

# 2️⃣ ПРОВЕРКА ТИПОВ
print(type(age))        # Вывод: <class 'int'>
print(type(name))       # Вывод: <class 'str'>

# 3️⃣ ПРЕОБРАЗОВАНИЕ ТИПОВ (КАСТИНГ)
year_str = "2024"
year_int = int(year_str)       # "2024" → 2024 (число)
price = 19.99
price_rounded = int(price)     # 19.99 → 19 (дробная часть отбрасывается!)

# 4️⃣ СЦЕПИВАНИЕ СТРОК И ЧИСЕЛ
# ❌ Ошибка: print("Мне " + age + " лет") → TypeError!
# ✅ Решение 1 (через str()):
msg1 = "Мне " + str(age) + " лет."
# ✅ Решение 2 (f-строка, современный стандарт Python):
msg2 = f"Меня зовут {name}, мне {age} лет, рост {height} м."

print(msg1)
print(msg2)