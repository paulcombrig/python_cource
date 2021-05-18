# Задание 1

# . Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.

class Matrix:

    def __init__(self, get_matrix):
        self.input = get_matrix

    def __add__(self, other):
        if len(self.input) == len(other.input):
            zipped_lines = zip(self.input, other.input)
            for string_1, string_2 in zipped_lines:
                if len(string_1) != len (string_2):
                    print('Wrong matrix definition')

                new_matrix_line = [elem_1 + elem_2 for elem_1, elem_2 in zip(string_1, string_2)]
                print(new_matrix_line)

        else:
            print('Wrong matrix definition')

matrix_1 = Matrix([[11, 3], [13, 5], [7, 8]])
matrix_2 = Matrix([[2, 9], [2, 88], [66, 7], [0, 4]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)

matrix_3 = Matrix([[11, 3], [13, 5], [7, 8]])
matrix_4 = Matrix([[2, 9], [2, 88],  [0, 4]])
print(matrix_3)
print(matrix_4)
print(matrix_3 + matrix_4)

