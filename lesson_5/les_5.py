# СПИСКИ
tasks = ["Купить хлеб", "Позвонить маме"]
tasks.append("Сделать ДЗ")      # Добавить в конец
tasks[0] = "Купить батон"       # Изменить по индексу
"ДЗ" in tasks                   # Проверить наличие → True

# СЛОВАРИ
user = {"name": "Анна", "age": 25, "is_premium": True}
user["age"] = 26                # Обновить значение
user["city"] = "Москва"         # Добавить новый ключ
print(user.get("email", "Не указан"))  # Безопасное получение (не упадёт, если ключа нет)

# СПИСОК СЛОВАРЕЙ - частая структура для данных ИИ
users = [
    {"id": 1, "name": "Анна", "role": "admin"},
    {"id": 2, "name": "Борис", "role": "user"},
    {"id": 3, "name": "Вика", "role": "user"},
]

# Найти всех пользователей с ролью "user"
regular_users = []
for user in users:
    if user["role"] == "user":
        regular_users.append(user["name"])

print(regular_users)


# ГРУППИРОВКА ДАННЫХ (словарь-аккумулятор)
logs = ["error", "info", "error", "warning", "info"]
stats = {}

for level in logs:
  if level in stats:
    stats[level] += 1 # Увеличиваем счетчик
  else:
    stats[level] = 1

# более питонический способ:
#   stats[level] = stats.get(level, 0) + 1

print(stats)  # -> {'error':2, 'info': 2, 'warning': 1}

# ПОИСК ПО СЛОВАРЮ (без цикла)
contacts = {
    "мама": "+79172675344",
    "работа": "+79172925369",
}

# вместо цикла для поиска:
print(contacts.get("папа")) # -> None
print(contacts)
