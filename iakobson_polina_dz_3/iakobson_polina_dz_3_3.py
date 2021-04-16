# Задание 3
# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

def thesaurus(*user_names):
    user_dict = dict()
    for each in user_names:
        user_dict.setdefault(each[0], [])
        user_dict[each[0]].append(each)
    return user_dict

print(thesaurus("Jurgen", "Maria", "Jonas", "Daniela"))