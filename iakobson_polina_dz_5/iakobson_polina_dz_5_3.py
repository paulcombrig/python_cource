# Задание 3
# Перебрать и вывести кортежи матрицы, составленной из двух списков:

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

import itertools
gen = ((tutor, klass) for tutor, klass in itertools.zip_longest(tutors, klasses))
for tutor,klass in itertools.zip_longest(tutors, klasses):
    print(f'{tutor}, {klass}, {type(gen)}')
