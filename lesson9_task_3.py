class Worker:
    def __init__(self):
        self.name = 'Ivan'
        self.surname = 'Petrov'
        self.position = 'Housekeeper'
        self.income = {'wage': 40000, 'bonus': 10000}


class Position(Worker):
    def get_full_name(self):
        return print(self.name, self.surname)

    def get_total_income(self):
        return print(f'Total income = {sum(self.income.values())}')


a = Position()
a.get_full_name()
a.get_total_income()
