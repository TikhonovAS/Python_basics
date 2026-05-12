# Задача: Функция принимает пароль и минимальную длину (по умолчанию 6).
# Возвращает True, если длина пароля >= min_Length, иначе False.
# Не используйте print внутри функции!

def check_password(password, min_length=6):
    return len(password) >= min_length


print(check_password("12345"))
print(check_password("secure123"))
print(check_password("abc", 3))