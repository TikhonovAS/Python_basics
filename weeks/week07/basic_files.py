# Задача:
# Сохраните файлы ниже.
# Заполните TODO самостоятельно
# Запускайте по очереди

# 1. Запись лога (перезапись)
with open("agent.log_2", "w", encoding="utf-8") as f:
    f.write("[INFO] Агент запущен.\n")
    f.write("[WARNING] Внимание! Важная информация!\n")
    f.write("[ERROR] Критическая ошибка!\n")

# 2. Чтение лога
with open("agent.log_2", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# 3. Добавление без стирания
with open("agent.log_2", "a", encoding="utf-8") as f:
    f.write("[INFO] Цикл обучения завершен.\n")
