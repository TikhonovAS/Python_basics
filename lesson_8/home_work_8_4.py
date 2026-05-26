"""
Задание 3. Безопасный ридер
Напишите функцию read_config(path), которая:
Пытается открыть и прочитать JSON-файл
При FileNotFoundError → создаёт файл с пустым словарём {} и возвращает его
При json.JSONDecodeError (файл повреждён) → возвращает "⚠️ Файл повреждён, создан резерв" и сохраняет {}
"""
import json


def read_config(path="config.json"):
  """
  Безопасно читает JSON-файл конфигурации.
  Если файл отсутствует - создает его пустым словарем {} и возвращает его.
  """
  try:
    # 1. Пытаемся открыть и распарсить JSON
    with open(path, "r", encoding="utf-8") as f:
      config = json.load(f)
    print(f"Конфиг загружен из '{path}'")
    return config

  except FileNotFoundError:
    # 2. Файла нет -> создаем пустой конфиг и возвращаем его
    print(f"Файл '{path}' не найден. Создаю пустой конфиг.")
    empty_config = {}
    with open(path, "w", encoding="utf-8") as f:
      json.dump(empty_config, f, indent=2, ensure_ascii=False)
    return empty_config

  except json.JSONDecodeError as e:
    print(f"Файл '{path}' поврежден или не в формате JSON. Ошибка: {e}")
    print("Перезаписываю пустым конфигом...")
    empty_config = {}
    with open(path, "w", encoding="utf-8") as f:
      json.dump(empty_config, f, indent=2, ensure_ascii=False)
    return empty_config

  except Exception as e:
    print(f"Неожиданная ошибка при чтении '{path}': {e}")
    return {}

# ТЕСТИРОВАНИЕ
# Тест 1: Файла еще нет -> сработает except FileNotFoundError
config_1 = read_config("test_config.json")
print("Результат1:", config_1)

# Тест 2: Файл уже создан -> сработает try (обычная загрузка)
config_2 = read_config("test_config.json")
print("Результат 2:", config_2)

# Сначала создадим валидный файл
print("--- Тест 1: Валидный JSON ---")
with open("test_config.json", "w", encoding="utf-8") as f:
  json.dump({"theme": "dark"}, f, indent=2, ensure_ascii=False)

read_config("test_config.json")

# Имитируем повреждение файла (ломаем синтаксис JSON)
print("\n--- Тест 2: Поврежденный JSON ---")
with open("test_config.json", "w", encoding="utf-8") as f:
  f.write("{broken json!!! не закрыта скобка")

read_config("test_config.json")

