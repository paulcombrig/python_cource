# Задание 6 - read
# Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом командной
# строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной
# строки значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
#        просто запуск скрипта — выводить все записи;
#        запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
#        запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
#        равный второму числу, включительно.

import sys
quantity_args = sys.argv[1:]

with open('bakery_sales.csv', encoding='utf-8') as file:
    if len(quantity_args) == 0:
        start_idx = 0
        end_idx = sum(1 for line in file)
        file.seek(0)
    elif len(quantity_args) == 1:
        start_idx = int(quantity_args[0])
        end_idx = sum(1 for line in file)
        file.seek(0)
    elif len(quantity_args) > 1:
        start_idx = int(quantity_args[0])
        end_idx = int(quantity_args[1])

    for idx, line in enumerate(file):
        if start_idx <= idx + 1 <= end_idx:
            print(line.strip())