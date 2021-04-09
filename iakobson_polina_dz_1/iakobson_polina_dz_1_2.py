# Задание 2
# Создать список, состоящий из кубов нечётных чисел от 0 до 1000
# 1. Составляем список из кубов нечетных чисел:
# 2. В одном цикле для каждого числа проверяем условия, что:
# - его куб без остатка делится на 7, в случае истины сумма цифр куба складывается с суммой №1
# - сумма кубла и 17 без остатка делится на 7, в случае истины сумма цифр куба складывается с суммой №2.
# 3. Вывести суммы на экран

# 1.
odds_list = []
for num in range(1, 1001, 2):
    odds_list.append(num ** 3)
# 2.
first_sum = 0
second_sum = 0
for num in odds_list:
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        first_sum += num
    num += 17
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        second_sum += num
# 3.
print(first_sum, ',', second_sum)