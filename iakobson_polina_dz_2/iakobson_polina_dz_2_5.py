# Задание 5.
# Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в
# виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить
# рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
# (должно быть 07 коп или 00 коп).

# В первом случае сделала вывод копеек в любом случае
price_list = [53.6, 15, 955, 17.12, 59.9, 22, 23, 67.81, 11.6, 120]
for each_price in price_list:
    int_price = int(each_price)
    float_price = round((each_price - int_price) * 100)
    print(f'{int_price} руб {float_price:02} коп')

# Во втором - только когда они есть
price_list = [53.6, 15, 955, 17.12, 59.9, 22, 23, 67.81, 11.6, 120]
print(f' ')
print(f'Другой вариант составления списка')
for each_price in price_list:
    int_price = int(each_price)
    float_price = (each_price - int_price) * 100
    round_float_price = round(float_price)
    if float_price != 0:
        print(f'{int_price} руб {round_float_price:02} коп')
    else:
        print(f'{int_price} руб')