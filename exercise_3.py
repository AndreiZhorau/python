class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name, self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


worker_1 = Position('Сергей', 'Сергеев', 'водитель', 1, 2)

print(worker_1.get_full_name())

print(worker_1.get_total_income())
