import requests

from src.abs_classes import API


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
            result = []
            for page in range(pages):
                req = requests.get(self._url, params={
                    'text': f'NAME:{profession}',
                    'page': page,
                    'per_page:': 20})
                data = req.json()
                result.extend(data.get('items'))
            return result
        except TypeError:
            print('Проблема с доступом к API HeadHunter')
