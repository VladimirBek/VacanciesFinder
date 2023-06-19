class Vacancy:
    vacancy_list = []

    def __init__(self, id, employer, title, salary, area, url):
        self.id = id
        self.employer = employer
        self.title = title
        self.salary = salary
        self.city = area
        self.url = url
        self.vacancy_list.append(self)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id, self.employer, self.title, self.salary, self.description})'

    def __lt__(self, other):
        return int(self.salary) < int(other.salary)

    def __le__(self, other):
        return int(self.salary) <= int(other.salary)
