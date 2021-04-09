# Задание 1
# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах

print('Для расчета длительности введите значение в секундах.')
duration_user_request = input('Длительность в секундах: ')
duration = int(duration_user_request)
minutes = duration // 60
seconds = duration - minutes * 60
print(minutes, 'мин', seconds, 'с')

