# Задание 1.
# Создать функцию перевода числительных с английского на русский
# Реализовала запрос ввода данных от пользователя и вывод найденного значения

dictionary = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}
input_name = input('Введите число на латинице')

def num_translate(input_name):
    name = input_name.strip(' ')
    if name in dictionary.keys():
        text = f'"{dictionary[name]}" - это русский перевод с английского "{name}"'
        return text
    else:
        text = 'Такого числа мы ещё не перевели'
        return text

print(num_translate(input_name))