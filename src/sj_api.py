import os

import requests

from src.abs_classes import API
from src.vacancy import Vacancy


class SuperJobAPI(API):
    """
    Метод для работы с API Super Job
    """

    def __init__(self):
        self._url = "https://api.superjob.ru/2.0/vacancies/"
        self._headers = {'X-Api-App-Id': os.environ.get('SJ_API_KEY')}

    def get_vacancies(self, profession: str) -> list:
        """
        Метод для получения списка вакансий по ключевым словам
        :param profession: Ключевое слово для поиска вакансий (наименование профессии)
        :return: список вакансий
        """
        try:
            for page in range(5):
                req = requests.get(self._url, headers=self._headers,
                                   params={"count": 500, "page": page, "archive": False, 'keyword': profession})
                data = req.json()
                for vac in data['objects']:
                    try:
                        if vac["payment_from"] != 0 and vac["payment_to"] != 0:
                            payment = f'от {vac["payment_from"]} до {vac["payment_to"]} {vac["currency"]}'
                        elif vac["payment_from"] == 0 and vac["payment_to"] != 0:
                            payment = f'до {vac["payment_to"]} {vac["currency"]}'
                        elif vac["payment_from"] != 0 and vac["payment_to"] == 0:
                            payment = f'от {vac["payment_from"]} {vac["currency"]}'
                        elif vac["payment_from"] == 0 and vac["payment_to"] == 0:
                            payment = 'не указана'
                        else:
                            payment = 'не удалось определить'
                    except KeyError:
                        payment = 'не удалось определить'
                    try:
                        client = vac['client']['title']
                    except KeyError:
                        client = 'не удалось определить'
                    Vacancy(vac['id'], client, vac['profession'], payment, vac["town"]["title"],
                            vac['link'])
                print(f'Загружена страница {page + 1} из 5 с портала Super Job...')
            print('Все вакансии загружены!')
            return Vacancy.vacancy_list
        except KeyError:
            print('Ошибка при получении вакансий с портала Super Job')
        except TypeError:
            print('Ошибка при получении вакансий с портала Super Job')
