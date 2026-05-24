"""
Задание 1. Логгер действий
Напишите функцию log_action(message, filename='agent.log'), которая:
- Открывает файл в режиме добавления ('a')
- Добавляет строку в формате '[LOG] {message}\n'
- Печатает '✅ Запись добавлена'
"""
def log_action(message, filename="agent.log"):
  """
  Добавляет новую запись в конец лог-файла.
  Автоматически оборачивает текст в префикс [LOG] и добавляет перенос строки \n
  Если файл отсутствует - создает его.
  """
  # 1. Открываем файл в режиме добавления ('a')
  with open(filename, "a", encoding="utf-8") as f:
    # 2. Записываем отформатированную строку
    f.write(f"[LOG] {message}\n")
  print("Запись добавлена")


log_action("Привет файл!")
log_action("Вторая строка для проверки")


def read_log(filename="agent.log"):
  """
  Считывает все содержимое файла в одну строку.
  Возвращает сырой текст, включая символы переноса строк \n
  Подходит для быстрого вывода или передачи в другой обработчик.
  """
  # 1. Открываем файл для чтения ('r')
  with open(filename, "r", encoding="utf-8") as f:
    # 2. Считываем весь текст целиком
    content = f.read()

  print("Содержание файла: ")
  print(content)

read_log()


def read_log_as_list(filename="agent.log"):
  """
  Считывает файл построчно, очищает каждую строку от '\n' и лишних пробелов.
  Игнорирует пустые строки. Возвращает готовый список для анализа.
  """
  # 1. Открываем файл и читаем все строки в список
  with open(filename, "r", encoding="utf-8") as f:
    raw_lines = f.readlines()


  # 2. Очищаем данные: убираем '\n', пробелы и пустые строки
  clean_lines = []
  for line in raw_lines:
    line = line.strip()         # убирает '\n' и пробелы по краям
    if line:                    # пробпускает пустые строки
      clean_lines.append(line)

  print("Список записей: ", clean_lines)
  print(clean_lines)

Logs = read_log_as_list()


def log_action_safe(message, filename="agent.log"):
  """
  Безопасно добавляет запись в лог-файл.
  Ловит типичные ошибки работы с файловой системой и выводит понятные сообщения.
  """
  try:
    # 1. Пытаемся открыть файл и записать данные
    with open(filename, "a", encoding="utf-8") as f:
      f.write(f"[LOG] {message}\n")
    print("Запись")

  except FileNotFoundError:
    # 2. Срабатывает, если папки по указанному пути не существует
    print(f"Ошибка: папка для файла '{filename}' не найдена.")

  except PermissionError:
    # 3. Срабатывает, если нет прав на запись (например, в системные папки)
    print("Ошибка: нет прав для записи в '{filename}'.")

  except Exception as e:
    # 4. Ловит любые другие непредвиденные ошибки и показывает их текст
    print(f"Непредвиденная ошибка: {e}")


# Тест 1: Успешная запись(без ошибок)
log_action_safe("Тест с защитой пройден")

# Тест 2: Ошибка пути (папки 'fare_folder' не существует)
log_action_safe("Это не запишется", filename="fare_folder/log.txt")

# Тест 3: Ошибка прав(попробуем записать в корень диска)
log_action_safe("Доступ запрещен", filename="/root/secret.log")
