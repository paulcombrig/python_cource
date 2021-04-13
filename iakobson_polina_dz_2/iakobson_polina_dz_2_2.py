# Задание 2
# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Новый список не создавать! Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for each_fragment in original_list:
    if each_fragment.isdigit():
        fragment_index = original_list.index(each_fragment)
        original_list[fragment_index] = f'"{int(each_fragment):02}"'
    elif (each_fragment.startswith('+') or each_fragment.startswith('-')) and each_fragment[1:].isdigit():
        fragment_index = original_list.index(each_fragment)
        original_list[fragment_index] = f'"{each_fragment[0]}{int(each_fragment):02}"'
    else:
        fragment_index = original_list.index(each_fragment)
        original_list[fragment_index] = f'{str(each_fragment)}'

list_to_string = ' '.join(original_list)

print(list_to_string)