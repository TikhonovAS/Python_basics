login = input("Введите логин: ")
password = input("Введите пароль: ")

# Правильные данные (пока хардкодим)
CORRECT_LOGIN = "admin"
CORRECT_PASSWORD = "12345"

if login == CORRECT_LOGIN and password == CORRECT_PASSWORD:
    print("Вход выполнен успешно! Добро пожаловать.")
elif login != CORRECT_LOGIN:
    print("Неверный логин.")
elif password != CORRECT_PASSWORD:
    print("Неверный пароль.")
else:
    print("Произошла неизвестная ошибка.")