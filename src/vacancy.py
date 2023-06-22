class Vacancy:
    """
    Класс для работы с вакансиями
    """
    vacancy_list = []

    def __init__(self, id, employer, title, area, url, currency, salary_from=0, salary_to=0):
        self.id = id
        self.employer = employer
        self.title = title
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.area = area
        self.url = url
        self.vacancy_list.append(self)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'{self.__class__.__name__}(' \
               f'id={self.id}, ' \
               f'employer={self.employer}, ' \
               f'title={self.title}, ' \
               f'salary_from={self.salary_from}, ' \
               f'salary_to={self.salary_to}, ' \
               f'currency={self.currency}, ' \
               f'area={self.area}, ' \
               f'url={self.url})'

    def __lt__(self, other):
        if self.salary_to != 0 and self.salary_from != 0:
            return (int(self.salary_to) + int(self.salary_from) / 2) < (
                    int(other.salary_to) + int(other.salary_from) / 2)
        elif self.salary_to == 0 and self.salary_from != 0:
            return int(self.salary_from) < int(other.salary_from)
        elif self.salary_to != 0 and self.salary_from == 0:
            return int(self.salary_to) < int(other.salary_to)
        else:
            return int(self.salary_to) < int(other.salary_to)

    def __le__(self, other):
        if self.salary_to != 0 and self.salary_from != 0:
            return (int(self.salary_to) + int(self.salary_from) / 2) <= (
                    int(other.salary_to) + int(other.salary_from) / 2)
        elif self.salary_to == 0 and self.salary_from != 0:
            return int(self.salary_from) <= int(other.salary_from)
        elif self.salary_to != 0 and self.salary_from == 0:
            return int(self.salary_to) <= int(other.salary_to)
        else:
            return int(self.salary_to) <= int(other.salary_to)
