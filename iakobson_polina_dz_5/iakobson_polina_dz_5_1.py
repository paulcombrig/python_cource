# Задание 1
# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield.

def odd_nums(break_point):
    number = 1
    while number <= break_point:
        yield number
        number += 2
        if number == break_point + 2:
            print('...Stop iteration...')

for number in odd_nums(15):
    print(number)