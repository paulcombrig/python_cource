# Задание 3
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО,
# значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные. \
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре
# значение None. Если наоборот — выходим из скрипта с кодом «1».

import itertools, json
dict = {}
with open('users.csv', 'r', encoding='utf-8') as users:
    for user in users:
        user = user.replace(',', ' ')
        users.seek(0)
        with open('hobby.csv', 'r', encoding='utf-8') as hobby:
            hobby.seek(0)
            for each_user, user_hobby in itertools.zip_longest(users, hobby):
                dict[each_user] = user_hobby
with open('dict.json', 'w+', encoding='utf-8') as dictionary:
    json.dump(dict, dictionary)
print(dict)