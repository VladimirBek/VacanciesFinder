import requests

from abs_classes import API


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
        :return: json файл с запрашиваемыми вакансиями
        """

        req = requests.get(self._url, params={'text': f'NAME:{profession}', 'per_page': 100})
        data = req.json()
        pages = int(data['pages'])
        result = []
        for page in range(pages):
            req = requests.get(self._url, params={
                'text': f'NAME:{profession}',
                'page': page,
                'per_page:': 100})
            data = req.json()
            result.append(data.get('items'))
        return result
