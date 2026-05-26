import json
import os

config_path = "settings.json"

# Проверяем наличие файла settings.json
if os.path.exists(config_path):
    # если файл есть то в консоле выведет надпись "Конфиг загружен"
    with open(config_path, "a", encoding="utf-8") as f:
        config = json.load(f)
    print("Конфиг загружен")
# если файла нет, то запишем новый с указанными данными
else:
    config = {
        "agent_name": "TestBot",
        "version": "1.0",
        "debug": False
    }
    print("Создан файл")

# меняем debug c False на True
config["debug"] = True

# сохраняем файл
with open(config_path, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

# возвращаем строку в JSON и выводим текст в консоль
print("Текущие настройки:")
print(json.dumps(config, indent=2, ensure_ascii=False))