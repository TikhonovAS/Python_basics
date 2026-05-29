class SimpleAgent:
    """Чертеж для создания простых агентов"""

    def __init__(self, name):
        """Конструктор: вызывается при создании объекта."""
        print(f"Создаю нового агента по имени {name}...")

        # Создаем атрибуты (свойства), которые будут жить внутри этого объекта
        self.name = name
        self.memory = []
        self.messages_count = 0

    def say_hello(self):
        """Метод: действие, который может советшить агент"""
        self.messages_count += 1
        greeting = f"Привет! Я {self.name}. Я помню {len(self.memory)} фактов."
        return greeting

    def remember(self, fact):
        """Метод: добавление информации в память"""
        self.memory.append(fact)
        print(f"{self.name} запомнил {fact}")

# ИСПОЛЬЗОВАНИЕ (Создаем объекты по чертежу)
# 1. Создаем первого агента (вызывается __init__)
jarvis = SimpleAgent("Джарвис")

# 2. Создаем второго агента (независимо от первого)
friday = SimpleAgent("Пятница")

# 3. Джарвис что-то запоминает
jarvis.remember("Любит кофе")
jarvis.remember("Знает Python")

# 4. Пятница запоминает свое
friday.remember("Любит чай")

# 5. Проверяем состояние
print("\n-----Статус-----")
print(jarvis.say_hello())
print(friday.say_hello())

