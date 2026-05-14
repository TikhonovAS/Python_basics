import json
import os
from datetime import datetime

# 1. Логирования старта
with open("agent.log", "a", encoding="utf-8") as log_file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(f"[{timestamp}] Агент запущен\n")

# 2. Чтение или создание настроек
config_path = "agent_config.json"

if os.path.exists(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    print("Конфиг загружен из файла")
else:
    config = {
        "model": "gpt-4o-mini",
        "temperature": 0.7,
        "max_tokens": 1024
    }
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    print("Конфиг создан с дефолтными значениями")

#  3. Управление памятью агента
memory_path = "agent_memory.json"
memory = []

# Проверяем наличие файла перед чтением
if os.path.exists(memory_path):
    with open(memory_path, "r", encoding="utf-8") as f:
        memory = json.load(f)

# Формируем новое сообщение
new_message = {
    "role": "system",
    "content": "Ты помощник разработчика. Отвечай кратко.",
    "added_at": datetime.now().isoformat()
}

# Добавим сообщение в конец списка
memory.append(new_message)

# Перепишем файл
with open(memory_path, "w", encoding="utf-8") as f:
    json.dump(memory, f, indent=2, ensure_ascii=False)

# Защитная проверка: берем [-1] только если список не пуст
if memory:
    print(f"В памяти теперь {len(memory)} записей. Последняя: {memory[-1]['role']}")
else:
    print("Память пуста. Проверьте, вызывается ли метод append() перед сохранением.")