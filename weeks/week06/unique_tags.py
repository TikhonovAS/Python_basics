# Задача:
# 1. Даны 2 списка тегов из разных источников
# 2. Преобразовать их в множества
# 3. Найти общие теги (пересечения)
# 4. Найти уникальные теги (объединения)
# 5. Вывести оба результата в отсортированном виде (sorted())

source_1 = ["python", "ai", "langchain", "api", "ai"]
source_2 = ["fastapi", "python", "docker", "langchain"]

s_1, s_2 = set(source_1), set(source_2)
traversal = s_1 & s_2
union = s_1 | s_2

print("Общие:", sorted(traversal))
print("Все уникальные:", sorted(union))