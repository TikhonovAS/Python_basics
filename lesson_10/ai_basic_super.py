# ИИ-агент с логированием через декоратор

import time
import random
from datetime import datetime

# ----------------------------------------------
# 1. ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ: запись в лог-файл
# ----------------------------------------------
def log_action(message, filename="agent.log"):
  """
  Безопасно добавляет запись в лог-файла.
  Используется декораторами для аудита действий.
  """
  try:
    with open(filename, "a", encoding="utf-8") as f:
      # Добавляет временную метку для удобства отладки
      timestamp = datetime.now().strftime("%H:%M:%S")
      f.write(f"[{timestamp}] {message}\n")
  except Exception as e:
    print(f"Ошибка записи лога: {e}")


# ---------------------------------------------------------
# 2. ДЕКОРАТОР: логирует вызов любого метода с аргументами
# ---------------------------------------------------------
def track_call(func):
  """
  Декоратор для логирования вызовов методов.
  Записывет: имя метода, аргументы, время выполнения.
  """
  def wrapper(self, *args, **kwargs):
    # Логируем ВХОД в метод
    log_action(f"ВЫЗОВ: {func.__name__}(args={args}, kwargs={kwargs})")

    # Засекаем время начала
    start = time.time()

    # Вызываем оригинальный метод, пробрасывая self и все другие аргументы
    result  = func(self, *args, **kwargs)

    # Засекаем время окончания
    duration = time.time() - start

    # Логируем ВЫХОД из метода + время выполнения
    log_action(f"ЗАВЕРШЕНО: {func.__name__} за {duration:.2f} сек. | Результат: {str(result)[:50]}...")

    # Возвращаем результат, как если бы декоратора не было
    return result

  return wrapper


# -------------------------------------------------------------
# 3. КЛАСС: ИИ-агент с логированием
# -------------------------------------------------------------
class MockAIAgent:
  """Имитация ИИ с автоматическим логированием всех действий"""
  def __init__(self, name="MockBot"):
    self.name = name
    self.history = []
    # Логируем создание агента (без декоратора, т.к. __init__ не декорируют)
    log_action(f"СОЗДАН АГЕНТ: {name}")
    print(f"Агент '{self.name}' инициализирован.")

  @track_call           # <-- Декоратор автоматически обернет этот метод
  def ask(self, question):
    """Принимает вопрос, имитирует 'мышление', возвращает ответ"""
    print(f"{self.name} думает...")
    time.sleep(2)       # Имитация задержки

    answers = [
        "Рекурсия - это когда функция вызывает саму себя, как матрешку.",
        "Рекурсия требует базового случае, иначе будет бесконечный цикл.",
        "Зеркало напротив зеркала - визуальная рекурсия.",
        "В программировании рекурсия - альтернатива циклам."
    ]
    answer = random.choice(answers)

    # Сохраняем в историю
    self.history.append({"role": "user", "content": question})
    self.history.append({"role": "assistant", "content": answer})

    return answer

  @track_call
  def get_history(self):
    """Возвращает историю диалога"""
    return self.history

  @track_call
  def get_stats(self):
    """Возвращает количество сообщений"""
    return {
      "name": self.name,
      "message_count": len(self.history),
      "last_activity": datetime.now().strftime("%H, %M, %S")
    }

  @track_call
  def clear_history(self):
    """Очищает историю диалога"""
    self.history = []
    log_action(f"{self.name} очистил память")
    print(f"{self.name} очистил память.")


# --------------------------------------------
# 4. ТОЧКА ВХОДА: тестовый сценарий
# --------------------------------------------
if __name__ == "__main__":
  print("Запускаем тест ИИ-агента с логированием...\n")

  # Создаем агента
  bot = MockAIAgent("Логгер-Бот")

  # Задаем вопросы
  print("\n--- Вопрос 1 ---")
  ans1 = bot.ask("Что такое рекурсия?")
  print(f"Ответ: {ans1}")

  print("\n--- Вопрос 2 ---")
  ans2 = bot.ask("Что такое цикл while?")
  print(f"Ответ: {ans2}")

  # Проверяем историю
  print("\n--- История диалога ---")
  for msg in bot.get_history():
    print(f"[{msg['role']}]: {msg['content']}")

  # Вывод статистики
  print("\n--- Статистика ---")
  stats = bot.get_stats()
  print(stats)

  # Очищаем память
  print("\n--- Очистка ---")
  bot.clear_history()

  print("\nТест завершен! Проверь файл agent.log - там вся история вызовов.")