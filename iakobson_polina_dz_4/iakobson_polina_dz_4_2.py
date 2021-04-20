# Задание 2

# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (USD, EUR, ...) ++
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.

import requests

currency = input('Введите название валюты ')


def currency_rates(currency):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if currency not in response:
        return f"ОШИБКА"
    else:
        required_currency = response[response.find('<Value>', response.find(currency)) + 7:response.find('</Value>',
                                                                                                         response.find(
                                                                                                             currency))]
        return required_currency

print(currency_rates(currency))
