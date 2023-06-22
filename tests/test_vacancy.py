from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy


def test_vacancy():
    hh = HeadHunterAPI()
    hh.get_vacancies('Адвокат по уголовным делам')
    vacancies = Vacancy.vacancy_list
    print(repr(vacancies[0]))
    print(repr(vacancies[1]))
    assert repr(vacancies[0]) == "Vacancy(id=82064177, employer=Международная Коллегия Адвокатов Города Москвы " \
                                 "Почуев, Зельгин и Партнеры, title=Юрист (помощник адвоката), salary_from=45000, " \
                                 "salary_to=70000, currency=RUR, area=Москва, url=https://hh.ru/vacancy/82064177)"
    assert str(vacancies[0]) == 'Юрист (помощник адвоката)'
    assert vacancies[0] < vacancies[1]
