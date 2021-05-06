# Задание 3
#
# Реализовать базовый класс Worker (работник):
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income)

class Worker:
    def __init__(self, name, surname, position, inc, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = inc
        self.inc = {'wage': wage, 'bonus': bonus}

    def get_salary(self, total=0):
        for each_key in self.inc.keys():
            total = total + self.inc[each_key]
        return total

class Position(Worker):
    def get_full_name(self):
        full_name = f'{super().name} {super().surname}'
        return full_name

    def get_total_income(self, total_income=0):
        total_income = super().get_salary()
        return total_income

position = Position('Irina', 'Pavlova', 'Manager', 0, 105000, 25000)
print(f'Salary of the {position.position}, {position.name} {position.surname}, is {position.get_total_income()} RUR.')
