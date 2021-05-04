# Задание 3
# Написать декоратор для логирования типов позиционных аргументов функции.

def type_logger(func):
    def type_wrapper(*args):
        arg_type = func(*args)
        for arg in args:
            print(f'{func.__name__}, {arg}: {type(arg_type)}')
        return arg_type
    return type_wrapper


@type_logger
def calc_cube(*args_x):
   for each_x in args_x:
       num_x = each_x ** 3
       return num_x

type_x = calc_cube(3, 8, 90)
print(type_x)
