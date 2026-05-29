"""
Напиши класс Robot со следующими требованиями:
Конструктор __init__: принимает model_name и battery_level (по умолчанию 100). Сохраняет их в self.
Метод work():
Если battery_level > 0: уменьшает заряд на 10, печатает "Робот работает... Осталось {battery_level}%".
Если battery_level == 0: печатает "Батарейка села! Нужна зарядка".
Метод charge(): восстанавливает заряд до 100 и печатает "Зарядка завершена".
"""


class Robot():
    """Mодель для создания клонов"""

    def __init__(self, model_name, battery_level=100):
        """Конструктор: принимает имя и начольный заряд (по умолчанию 100)"""
        self.model_name = model_name
        self.battery_level = battery_level
        print(f"Создан робот по имени '{self.model_name}'. Заряд: {self.battery_level} %")

    def work(self):
        """Метод, уменьшающий заряд на 10 и выводящий остаток заряда в консоль"""
        if self.battery_level > 0:
            self.battery_level -= 10
            print(f"Робот работает...Осталось {self.battery_level} %")
        else:
            print("Батарейка села! Нужна зарядка")

    def charge(self):
        """Метод, восстанавливающий заряд до 100 % и выводящий 'Зарядка завершена'"""
        self.battery_level = 100
        print("Зарядка завершена! Заряд 100 %")

    def respond(self):
        print("Бип-бип! Я обычный робот.")

# ТЕСТИРОВАНИЕ

# my_bot = Robot("R2-D2")
# my_bot.work()
# my_bot.work()
# my_bot.charge()
# my_bot.work()

class SmartRobot(Robot):  # <-- в скобках указываем РОДИТЕЛЯ
    """Умный робот, наследует все от Robot, но знает Python"""

    def __init__(self, model_name, battery_level=100):
        # super() передает имя и заряд в конструктор родительского класса Robot
        super().__init__(model_name, battery_level)

        # Добавляем новое свойство, которого нет у обычного робота
        self.knowledge_base = []
        print(f"{self.model_name} инициализирован с интелектом.")

    def learn(self, topic):
        """Новый метод: робот учит что-то новое"""
        self.knowledge_base.append(topic)
        print(f"{self.model_name} выучил {topic}")

    def show_skills(self):
        """Метод, испоьзующий атрибуты родителя и свои"""
        # Мы можем использовать self.name, потому что он есть у Робота
        print(f"Я {self.model_name}. Мой заряд: {self.battery_level}%.")
        print(f"Я знаю: {self.knowledge_base}")

    def respond(self):
        print("Я обрабатываю запрос... Готово!")


# # ТЕСТирование

# # Создаем умного робота
# brain_bot = SmartRobot("Brainy", battery_level=50)
#
# # Он работает как обычный робот (наследие)
# brain_bot.work()
# brain_bot.charge()
#
# # но он умеет больше
# brain_bot.learn("Python Basics")
# brain_bot.learn("Neural Networks")
#
# brain_bot.show_skills()

# --------------home_work----------------
"""
Напиши класс RobotWithCamera, который наследуется от Robot.
Требования:
Конструктор: принимает model_name, battery_level и новый параметр resolution (например, "1080p").
Обязательно используй super(), чтобы передать имя и батарею родителю.
Сохрани resolution в self.resolution.
Метод take_photo(): печатает '📸 Снимок сделан! Качество: {self.resolution}'.
"""
class RobotWithCamera(Robot):
    """Умный робот, наследует все от Robot, но  еще умеет делать фото"""
    def __init__(self, model_name, battery_level=100, resolution="1080p"):
        """super() передает имя и заряд в конструктор родительского класса Robot"""
        super().__init__(model_name, battery_level)

        # Добавляем новое свойство
        """Устанавливает качество снимка"""
        self.resolution = resolution

    def take_photo(self):
        """Отчет о том что сделан снимок"""
        print(f"Снимок сделан! Качество: {self.resolution}")

    def respond(self):
        print("Камера активна. Передаю видеопоток.")


# Тестирование

# # Создаем робота с камерой
# photo_bot = RobotWithCamera("PhotoBot", 80, "4K")
#
# # Проверяем наследие (зарядка)
# photo_bot.work()
# photo_bot.work()
#
# # Проверяем новую функцию
# photo_bot.take_photo()

def run_diagnostics(agent):
    """Принимает любой объект, у которого есть методы work() и respond()"""
    print(f"Тестируем: {agent.model_name}")
    agent.work()
    agent.respond()
    print("-" * 30)

# Тестирование
#
# # 3. Создаём разных роботов
# r1 = Robot("Basic-1")
# r2 = SmartRobot("AI-Brain")
# r3 = RobotWithCamera("Cam-Pro", 100, "4K")
#
# # 4. Прогоняем через ОДНУ и ту же функцию
# run_diagnostics(r1)
# run_diagnostics(r2)
# run_diagnostics(r3)

def log_action(message, filename="agent.log"):
    """Безопасно добавляет запись в лог-файл"""
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"[LOG] {message}\n")
    except Exception as e:
        print(f"Ошибка записи лога: {e}")


def track_method(func):
    """Декоратор: логирует вызов любого метода класса"""
    def wrapper(self, *args, **kwargs):
        # 1. Логируем факт вызова
        log_action(f"Метод '{func.__name__}' запущен")


        # 2. Запускаем сам метод, пробрасывая self и все аргументы
        result = func(self, *args, **kwargs)

        # 3. Возвращаем результат (важно!)
        return result
    return wrapper

class AgentManager:
    """Диспетчерская, которая хранит список роботов и управляет ими центрользованно"""
    def __init__(self):
        """Список, где будут лежать все роботы"""
        self.agents = []
        log_action("Менеджер создан")

    def add_agent(self, agent):
        """Добаляет робота в список"""
        self.agents.append(agent)
        log_action(f"{agent.model_name} добавлен в пул.")

    @track_method
    def start_shift(self):
        """
        Запускает смену для всех роботов в списке
        """
        print("\n----- НАЧАЛО СМЕНЫ ------")
        for agent in self.agents:
            print(f"Команда для: {agent.model_name}")
            agent.work()    # Каждый робот тратит заряд по-своему
            agent.respond() # Каждый робот отвечает по-своему
            print("-" * 30)

    @track_method
    def report_battery(self):
        """Выводит отчет по заряду всех роботов"""
        print("\n-------- ОТЧЕТ ЗАРЯДА ----------")
        for agent in self.agents:
            print(f"{agent.model_name}: {agent.battery_level}%")
        print("-" * 30)

"""Напиши код использования этого менеджера. Это не новые классы, а просто сценарий запуска.
Требования:
Создай экземпляр менеджера: manager = AgentManager()
Создай двух роботов:
Обычного: Robot("Unit-1")
Умного: SmartRobot("AI-X", 50) (с зарядом 50, чтобы видеть разницу)
Добавь их обоих в менеджера через manager.add_agent(...).
Запусти смену: manager.start_shift().
Сделай отчёт: manager.report_battery().
💡 Подсказка: Убедись, что у твоих классов есть метод respond(), который мы добавляли в шаге с 
полиморфизмом. Если его нет, добавь заглушку print("...") внутрь классов, чтобы код не падал.
"""
manager = AgentManager()
r1 = Robot("Unit-1")
r2 = SmartRobot("AI-X", 50)

manager.add_agent(r1)
manager.add_agent(r2)

manager.start_shift()
manager.report_battery()
