import os

import requests

from src.abs_classes import API


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
            result = []
            for page in range(5):
                req = requests.get(self._url, headers=self._headers,
                                   params={"count": 500, "page": page, "archive": False, 'keyword': profession})
                data = req.json()
                result.extend(data['objects'])
            return result
        except KeyError:
            print('Ошибка при получении вакансий с портала Super Job')
