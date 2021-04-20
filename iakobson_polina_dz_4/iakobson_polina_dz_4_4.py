# Задание 4
# Перенести currency_rates() в отдельный модуль utils и несколько раз вызвать его
# Это модуль вызова функции через импорт

import utils

print(utils.currency_rates('EUR'))
print(utils.currency_rates('ZAR'))
print(utils.currency_rates('JPY'))
print(utils.currency_rates('CZK'))
print(utils.currency_rates('CHF'))
print(utils.currency_rates('РУБ'))




