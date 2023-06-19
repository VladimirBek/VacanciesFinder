import requests

from src.abs_classes import API
from src.vacancy import Vacancy


class HeadHunterAPI(API):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self._url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, profession: str) -> list:
        """
        Метод для получения списка вакансий по API HeadHunter
        :param profession: Наименование профессии по которой следует провести поиск
        :return: список с запрашиваемыми вакансиями
        """
        try:
            req = requests.get(self._url, params={'text': f'NAME:{profession}', 'per_page': 20})
            data = req.json()
            pages = int(data['pages'])
            for page in range(pages):
                req = requests.get(self._url, params={
                    'text': f'NAME:{profession}',
                    'page': page,
                    'per_page:': 20})
                data = req.json()
                for vac in data['items']:
                    try:

                        if isinstance(vac['salary']['from'], int) and isinstance(vac['salary']['to'], int):
                            salary = f"от {vac['salary']['from']} до {vac['salary']['to']} {vac['salary']['currency']}"
                        elif not isinstance(vac['salary']['from'], int) and isinstance(vac['salary']['to'], int):
                            salary = f"до {vac['salary']['to']} {vac['salary']['currency']}"
                        elif isinstance(vac['salary']['from'], int) and not isinstance(vac['salary']['to'], int):
                            salary = f"от {vac['salary']['to']} {vac['salary']['currency']}"
                        elif not isinstance(vac['salary']['from'], int) and not isinstance(vac['salary']['to'], int):
                            salary = "не указана"
                        else:
                            salary = "не удалось определить"
                    except TypeError:
                        salary = "не удалось определить"
                    Vacancy(vac['id'], vac['employer']['name'], vac['name'], salary, vac['area']['name'],
                            vac['alternate_url'])
                print(f'Загружена страница {page+1} из {pages} с портала Head Hunter...')
            else:
                print('Все вакансии успешно загружены!')
            return Vacancy.vacancy_list
        except TypeError:
            print('Проблема с доступом к API HeadHunter')
