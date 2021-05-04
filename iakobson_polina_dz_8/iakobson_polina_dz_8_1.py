# Задание 1
# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
#
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru

import re

RE_VALID_EMAIL = re.compile(r'([a-z0-9_]+)@([a-z0-9]+\.[a-z]+)$')

def email_parse(email):
    dict_emails_hosts = {}
    entered_email = RE_VALID_EMAIL.findall(email)
    #    print(entered_email)
    if entered_email:
        for login, host in entered_email:
            dict_emails_hosts[login] = host
            print(dict_emails_hosts)
    else:
        raise ValueError(f'Извините, введенный электронный адрес {email} некорректен')


email_parse('someone@geekbrains.ru')
email_parse('correct@10mail.com')
email_parse('in_correct@yahoocom')
email_parse('noone_mail.ru')
email_parse('mailto:nobody@gmail.com')
email_parse('2go2@mail.ru')
