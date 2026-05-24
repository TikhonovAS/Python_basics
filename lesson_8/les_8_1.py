import json

# Словарь -> JSON строка
data = {"name": "Агент", "version": 1.2}
json_str = json.dumps(data, indent=2, ensure_ascii=False)

# JSON файл -> Словарь
with open("config.json", "r") as f:
  config = json.load(f)