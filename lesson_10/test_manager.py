import pytest
import os
import json
from agent_manager import AgentManager, MockAIAgent   # Импортируем наши классы

# Путь к тестовому файлу (чтобы не смешивать с основным history.json)
TEST_JSON = "test_output.json"

@pytest.fixture
def manager():
  """Создает чистого менеджера перед каждым тестом"""
  return AgentManager()

def test_add_agent(manager):
  """Проверяет, что агент добавляется в список"""
  bot = MockAIAgent("TestBot")
  manager.add_agent(bot)

  # Проверяем, что в списке manager.agents теперь есть 1 элемент
  assert len(manager.agents) == 1
  # Проверяем, что этот элемент - наш бот
  assert manager.agents[0].name == "TestBot"

def test_export_history(manager):
  """Проверяем, что метод export_history реально создает файл"""
  # 1. Добавляем бота, чтобы было что сохранить
  manager.add_agent(MockAIAgent("JsonBot"))

  # 2. Вызываем экспорт в тестовый файл
  manager.export_history(TEST_JSON)

  # 3. Проверяем, что файл появился на диске
  assert os.path.exists(TEST_JSON)

  # 4. Открываем и читаем содержимое
  with open(TEST_JSON, "r", encoding="utf-8") as f:
    data = json.load(f)

  # 5. Проверяем структуру данных
  assert "agents" in data
  assert len(data["agents"]) == 1
  assert data["agents"][0]["name"] == "JsonBot"

  # Убираем за собой (удаляем тестовый файл)
  os.remove(TEST_JSON)


# ==========================================================================================
# Чтобы запустить тест необходимо:
# 1. Перейти в папку lesson_10 (командой в терминале: cd lesson_10)
# 2. Ввести команду: poetry run pytest test_manager.py -v
