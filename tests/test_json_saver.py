from src.hh_api import HeadHunterAPI
from src.json_saver import JsonSaver
from src.vacancy import Vacancy


def test_get_info():
    js = JsonSaver()
    hh = HeadHunterAPI()
    hh.get_vacancies('Адвокат по уголовным делам')
    for vac in Vacancy.vacancy_list:
        js.add_vacancy(vac)
    assert isinstance(js.get_info(), list)


def test_del_vacancy():
    js = JsonSaver()
    hh = HeadHunterAPI()
    hh.get_vacancies('Адвокат по уголовным делам')
    for vac in Vacancy.vacancy_list:
        js.add_vacancy(vac)
    info = js.get_info()
    assert len(info) == 7
    js.del_vacancy(str(81849631))
    info = js.get_info()
    assert len(info) == 6


def test_filter_by_area():
    js = JsonSaver()
    hh = HeadHunterAPI()
    hh.get_vacancies('Адвокат по уголовным делам')
    for vac in Vacancy.vacancy_list:
        js.add_vacancy(vac)
    new_info = js.filter_by_area('Москва')
    assert len(new_info) == 3


def test_filter_by_salary():
    js = JsonSaver()
    hh = HeadHunterAPI()
    hh.get_vacancies('Адвокат по уголовным делам')
    for vac in Vacancy.vacancy_list:
        js.add_vacancy(vac)
    new_info = js.filter_by_salary(start=50000)
    assert len(new_info) == 2
    new_info = js.filter_by_salary(to=100000)
    assert len(new_info) == 6
    new_info = js.filter_by_salary(start=50000, to=100000)
    assert len(new_info) == 1


def test_sort_data():
    js = JsonSaver()
    hh = HeadHunterAPI()
    hh.get_vacancies('Адвокат по уголовным делам')
    for vac in Vacancy.vacancy_list:
        js.add_vacancy(vac)
    js.sort_data(1)
    new_info = js.get_info()
    assert new_info[0]['title'] == "Адвокат"
    js.sort_data(2)
    new_info = js.get_info()
    assert new_info[0]['id'] == "81539121"

