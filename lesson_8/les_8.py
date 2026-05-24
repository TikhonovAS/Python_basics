# 1. ЧТЕНИЕ
with open("data.txt", "r", encoding="utf-8") as f:
  content = f.read()     # Все содержимое
  lines = f.readlines()  # Список строк

# 2. ЗАПИСЬ (перезаписывает файл!)
with open("data.txt", "w", encoding="utf-8") as f:
  f.write("Привет, мир!\n")
  f.write("Вторая строка.\n")

# 3. ДОБАВЛЕНИЕ (в конец файла)
with open("data.txt", "a", encoding="utf-8") as f:
  f.write("Новая запись.\n")
