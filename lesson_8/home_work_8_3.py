# Задание 2. Конвертер данных
# Дан список пользователей: users = [{"id": 1, "name": "Анна"}, {"id": 2, "name": "Борис"}].
# Сохраните его в файл users.json в читаемом формате (indent=2).
# Затем напишите функцию read_users(), которая загружает этот файл и возвращает список словарей.
# """
import json

users = [{"id": 1, "name": "Анна"}, {"id": 2, "name": "Борис"}]
with open("users.json", "w", encoding="utf-8") as f:
  json.dump(users, f, indent=2, ensure_ascii=False)

print("Файл users.json создан!")


def read_users(filename="users.json"):
  """
  Загружает список пользователей из JSON-файла.
  Возвращает список словарей, готовый к обработке в Python.
  """
  # 1. Открываем файл для чтения
  with open(filename, "r", encoding="utf-8") as f:
    # 2. Превращаем JSON обратно в Python-объект (список словарей)
    users_list = json.load(f)


  print(f"Загружено пользователей: {len(users_list)}")
  return users_list

loaded_users = read_users()
print("Первый пользователь: ", loaded_users[0])
print("Имя второго: ", loaded_users[1]["name"])