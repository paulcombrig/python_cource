# Задание 4
# Вывести значения элементов списка, которые больше предыдущих.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

result = [val for idx, val in enumerate(src) if val > src[idx-1] and val != 300]
print(result)
