# 1️⃣ ОЧИСТКА И ПОДГОТОВКА ТЕКСТА (частая задача для ИИ)
raw_input = "  Hello, World!  "
clean = raw_input.strip().lower().replace(",", "")
print(f"Было: '{raw_input}'")   # '  Hello, World!  '
print(f"Стало: '{clean}'")      # 'hello world'

# 2️⃣ РАЗБОР ДАННЫХ ИЗ СТРОКИ
date_str = "2024-05-19"
year, month, day = date_str.split("-")  # unpacking
print(f"Год: {year}, Месяц: {month}")   # Год: 2024, Месяц: 05

# 3️⃣ ПОИСК И ПРОВЕРКА
email = "user@sky.pro"
if email.endswith("@sky.pro") and "@" in email:
    print("✅ Корпоративная почта")

# 4️⃣ ФОРМАТИРОВАНИЕ (вспоминаем f-строки)
name = "Анна"
score = 95.5
msg = f"Пользователь {name.capitalize()} набрал {score:.1f} баллов"
print(msg)  # Пользователь Анна набрал 95.5 баллов