import json

# 1. СОХРАНЕНИЕ НАСТРОЕК АГЕНТА
def save_agent_state(name, level, inventory):
  state = {"name": name, "level": level, "inventory": inventory}
  with open("agent_save.json", "w", incoding="utf-8") as f:
    json.dump(state, f, indent=2, ensure_ascii=False)
  print("Процесс сохранен!")

# 2. ЗАГРУЗКА С ПРОВЕРКОЙ НАЛИЧИЯ ФАЙЛА
import os

def load_agent_state():
  if not os.path.exists("agent_save.json"):
    return{"name": "Новичок", "level": 1, "inventory": []}

  with open("agent_save.json", "r", encoding="utf-8") as f:
    return json.load(f)

# 3. ПОСТРОЧНОЕ ЧТЕНИЕ (для логов)
def get_last_logs(filepath, count=3):
  try:
    with open(filepath, "r", encoding="utf-8") as f:
      lines = f.readlines()
    return lines[-count]                  # берем последние n-строк
  except FileNotFoundError:
    return ["Лог-файл не найден."]
