# Пример 1. Перебор списка
fruits = ["яблоко", "банан", "вишня"]

for fruit in fruits:
    print("Я люблю", fruit)

print("-" * 15)

# Пример 2. Создаем последовательность числа без списка
for i in  range(5):
    print(i)

print("-" * 15)

# Повторение по условию
count = 3

while count > 0:
    print("Осталось секунд:", count)
    count -= 1
print("Поехали!")
print("-" * 15)
