# Задание 3
# Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки.

word_stem = 'процент'
percent = int(input('Введите величину процента:'))
if percent >= 0:
    if percent in range(2, 5):
        word_end = 'а'
    elif percent in range(5, 20) or percent == 0:
        word_end = 'ов'
    else:
        word_end = ''
    print(percent, word_stem + word_end)
elif percent == ' ':
    print('Процент не может быть пустым')
else:
    print('Недопустимая величина процента')
