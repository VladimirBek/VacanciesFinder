
class Vacancy:

    def __init__(self, id, employer, title, salary, description):
        self.id = id
        self.employer = employer
        self.title = title
        self.salary = salary
        self.description = description

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id, self.employer, self.title, self.salary, self.description})'

    def __lt__(self, other):
        return int(self.salary) < int(other.salary)

    def __le__(self, other):
        return int(self.salary) <= int(other.salary)
