import json

def save_json(data, filename="config.json"):
  """
  Сохраняет словарь или список в JSON-файл.
  Автоматически форматирует вывод для читаемости и поддерживает кирилицу.
  """
  try:
    # 1. Открываем файл на запись
    with open(filename, "w", encoding="utf-8") as f:
      # 2. Преобразуем Python-объект в JSON и пишем в файл
      # indent=2 -> делает отступы для читаемости
      # ensure_ascii=False -> сохраняет русский текст как есть
      json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Данные сохранены в {filename}")

  except TypeError as e:
    print(f"Ошибка типа: JSON не поддерживает этот объект. {e}")
  except Exception as e:
    print(f"Ошибка записи: {e}")

def load_json(filename="config.json"):
  """
  Загружает данные из JSON-файла. Возвращает словарь/список.
  Если файла нет или он поврежден -> возвращает безопасное значение по умолчанию.
  """
  try:
    with open(filename, "r", encoding="utf-8") as f:
      data = json.load(f)  # Превращает JSON обратно в Python-объект
    print("Данные загружены из {filename}")
    return data

  except FileNotFoundError:
    print(f"Файл '{filename}' не найден. Возвращаем пустой словарь.")
    return {}
  except json.JSONDecodeError as e:
    print(f"Файл поврежден или не в формате JSON. {e}")
    return {}
  except Exception as e:
    print(f"Неожиданная ошибка загрузки: {e}")
    return {}

# Тестирование
# 1. Готовим данные (словарь с вложенными типами)
agent_config = {
    "name": "AI-Assistant",
    "version": 1.2,
    "skills": ["chat", "analyze", "log"],
    "settings": {"theme": "dark", "auto_save": True}
 }

# 2. Сохраняем
save_json(agent_config, "agent_data.json")

# 3. Загружаем обратно
loaded_config = load_json("agent_data.json")
print("Проверка загрузки: ", loaded_config["name"], loaded_config["settings"]["theme"])
