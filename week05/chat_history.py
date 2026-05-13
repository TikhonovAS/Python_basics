# Задача:
# 1. Создать пустой список
# 2. Добавить 2 словаря:{"role": "user", "content": "Привет"} и {"role": "assistant": "content": "Здравствуйте!"}
# 3. Написать цикл for, который выводит каждое сообщение в формате:
#   {user} Привет
#   {assistant} Здравствуйте!
# 4. Добавить навое сообщение в конец списка

message = []
message.append({"role": "user", "content": "Привет"})
message.append({"role": "assistant", "content": "Здравствуйте!"})

for msg in message:
    print(f"{msg['role']}: {msg['content']}")


message.append({"role": "user", "content": "Как дела?"})