# Задача:
# 1. Создать кортеж config = ("claude-3.5-sonnet", 0.2, 4096)
# 2. Распаковать его в переменные model, temp, max_tokens
# 3. Сформировать словарь настроек: {"model": ..., "temperature": ..., "max_tokens": ...}
# 4. Попробовать изменить config[1] = 0.5 -> убедитесь, что Python ругается
# 5. Вывести итоговый словарь

config = ("claude-3.5-sonnet", 0.2, 4096)
model, temp, max_tokens = config

setting = {
    "model": model,
    "temperature": temp,
    "max_tokens": max_tokens
}

# config[1] = 0.5   # -> TypeError: 'tuple' object does not support item assignment

print(setting)