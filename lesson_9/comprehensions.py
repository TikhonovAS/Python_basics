# 1. БАЗОВОЕ ВКЛЮЧЕНИЕ (фильтрация + преобразование)
raw_scores =[85, 42, 91, 15, 78, 100, 30]

# оставляем только проходные баллы (>= 50) и округляем до десятков
passed = [round(s / 10) * 10 for s in raw_scores if s >= 50]

print("Проходные: ", passed)

# 2. ГЕНЕРАТОР (экономия памяти, вместо [...] используем (...))
large_date_gen = (x * 2 for x in range(1_000_000))

print("Тип объекта: ", type(large_date_gen))
print("Первые 5 значений: ", list(large_date_gen)[:5])

# 3. ВЛОЖЕННЫЕ ВКЛЮЧЕНИЯ (плоский список из матрицы)
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)