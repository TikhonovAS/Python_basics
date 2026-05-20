# 1. ПРОСТАЯ ФУНКЦИЯ С ВОЗВРАТОМ
def calculate_bmi(weight, height):
    """Рассчитывает индекс массы тела"""
    bmi = weight / (height ** 2)
    return round(bmi, 2)


# Использование:
result = calculate_bmi(70, 1.75)
print(f"Ваш ИМТ: {result}")  # Ваш ИМТ: 22.86


# 2. ФУНКЦИЯ С ПАРАМЕТРОМ ПО УМОЛЧАНИЮ
def send_notification(message, priority="low"):
    """Отправляет уведомление с приоритетом"""
    if priority == "high":
        return f"🔥 СРОЧНО: {message}"
    return f"📩 {message}"


print(send_notification("Новое сообщение"))  # 📩 Новое сообщение
print(send_notification("Сервер упал", "high"))  # 🔥 СРОЧНО: Сервер упал


# 3️. ФУНКЦИЯ БЕЗ RETURN (только побочный эффект)
def log_action(action):
    """Записывает действие в лог (в реальности — в файл)"""
    print(f"[LOG] {action}")  # Печать — это побочный эффект
    # Нет return → функция вернёт None


result = log_action("Пользователь вошёл")
print(result)  # None (потому что функция ничего не вернула)


# 4️. ФУНКЦИЯ, КОТОРАЯ ВОЗВРАЩАЕТ НЕСКОЛЬКО ЗНАЧЕНИЙ
def parse_email(email):
    """Разбивает email на имя и домен"""
    if "@" not in email:
        return None, None  # Обработка ошибки
    name, domain = email.split("@")
    return name, domain  # Возвращаем кортеж из 2 значений


user, site = parse_email("admin@sky.pro")
print(f"Пользователь: {user}, Домен: {site}")  # admin, sky.pro
