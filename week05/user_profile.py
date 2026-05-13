# Задача:
# 1. Создать словарь profile с ключами: name, email, plan
# 2. Безопасно получить значение "phone" (вернуть "не указан")
# 3. Изменить plan на "premium"
# 4. Вывести все ключи и все значения отдельно

profile = {
    "name": "Мария",
    "email": "maria@test.ru",
    "plan": "free"
}

print(profile.get("phone", "не указан"))
profile["plan"] = "premium"

print("Ключи:", profile.keys())
print("Значения", profile.values())