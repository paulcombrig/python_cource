# Задание 1

# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#   |--settings
#   |--mainapp
#   |--adminapp
#   |--authapp

# Честно скажу, насчет использования json не знала, поэтому этот момент пришлось подглядеть(

import os

structure = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for parent, children in structure.items():
    if os.path.exists(parent):
        print(f'Папка {parent} уже существует')
    else:
        for each in children:
            current_folder = os.path.join(parent, each)
            if os.path.exists(current_folder):
                print(f'Папка {current_folder} существует')
            else:
                os.makedirs(current_folder)


