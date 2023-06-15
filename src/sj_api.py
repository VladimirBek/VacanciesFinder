import os

import requests

from src.abs_classes import API


class SuperJobAPI(API):
    """
    Метод для работы с API Super Job
    """

    def __init__(self):
        self._url = "https://api.superjob.ru/2.0/vacancies/"
        self._headers = {'X-Api-App-Id': os.getenv('SJ_API_KEY')}

    def get_vacancies(self, profession: str) -> list:
        req = requests.get(self._url, headers=self._headers,
                           params={"count": 100, "archive": False, 'keyword': profession})
        data = req.json()
        return data['objects']


sj_api = SuperJobAPI()
print(sj_api.get_vacancies('HR'))
