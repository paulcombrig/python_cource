# Задание 4
# Перенести currency_rates() в отдельный модуль utils и несколько раз вызвать его
# Это модуль описания импортируемой функции

import requests

def currency_rates(currency):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if currency not in response:
        return f"ОШИБКА"
    else:
        required_currency = response[response.find('<Value>', response.find(currency)) + 7:response.find('</Value>',
                                                                                                         response.find(
                                                                                                             currency))]
        return required_currency