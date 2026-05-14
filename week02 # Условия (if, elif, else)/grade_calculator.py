# Задача: Пользователь вводит баллы (0 - 100). Программа выводит букву оценки:
# 90 - 100 -> A, 80 - 89 -> B, 70 - 79 -> C, 60 - 69 -> D, < 60 -> F

score = int(input("Введите баллы (0 - 100): "))

if score > 100:
    grade = "Балл не должен быть больше 100"
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Ваша оценка: {grade}")