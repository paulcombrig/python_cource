# Задание 4
# Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }

import os

files = []
for roots, dirs, fls in os.walk('./'):
    for file in fls:
        file_path = os.path.join(roots, file)
        files.append(os.stat(file_path).st_size)
maximum = max(files)

i = 1
result = {}
for each in range(len(str(maximum))):
    i *= 10
    result[i] = 0
for file in files:
        result[10 ** len(str(file))] += 1

print(result)