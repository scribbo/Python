class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.n = name
        self.s = surname
        self.p = position
        self._income = {'wage': wage, 'bonus': bonus}
        self.w = wage
        self.b = bonus


class Position(Worker):
    def get_full_name(self):
        print(f'{self.n} {self.s}')

    def get_total_income(self):
        tot = self._income.get('wage') + self._income.get('bonus')
        print(tot)


person = Position('Иван', 'Иванович', 'стажер', 20000, 5000)
person.get_full_name()
person.get_total_income()
