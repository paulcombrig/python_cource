# Задание 1
# Распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# Уполучить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)

import requests


text = requests.get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text
with open('nginx_logs.txt', 'w+') as file:
    result = []
    file.write(text)
    file.seek(2)
    for each in file:
        split = each.split()
        result.append(f'{split[0]}, {split[5]}, {split[6]}')
print(result)