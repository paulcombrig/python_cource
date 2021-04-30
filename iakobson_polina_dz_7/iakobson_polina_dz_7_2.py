# Задание 3

# Написать скрипт, который собирает все шаблоны в одну папку templates.
# Примечание: исходные файлы необходимо оставить; обратите внимание,
# что html-файлы расположены в родительских папках (они играют роль пространств имён)

import os
import shutil
my_dir = 'iakobson_polina_dz_7'
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folder = r'my_project'
files = []

for roots, dirs, fls in os.walk(folder):
    for file in fls:
        if file.lower().endswith('.html'):
            files.append(os.path.join(roots, file))
for path in files:
    folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    target_dir = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, target_dir)
#html_files = [item for item in os.listdir(folder_path)
#               if item.endswith('.html')]
# target_folder = '../folder_path'
# for root, dirs, files in os.walk(folder_path):
#     for file in html_files:
#         shutil.copyfileobj(file, os.mkdir(target_folder))













