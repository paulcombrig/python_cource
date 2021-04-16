# Задание 5

# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов, взятых из трёх списков

# Хотела максимально оптимизировать код, но в итоге запуталась в списках. Выводит результат трёх итераций составления шуток, но все в одну строку.


import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

"""adding all the dictionaries in unity list"""

list_of_dictionaries = [nouns, adverbs, adjectives]

"""getting all the necessary values in two function"""

def get_random_choice(dictionary):
    random_element = random.choice(dictionary)
    return random_element

def get_jokes(num):
    phrase = []
    for each in range(num):
        for every_dictionary in list_of_dictionaries:
            choice = get_random_choice(every_dictionary)
            phrase.append(f'{choice}')
    return phrase

print(get_jokes(3))


