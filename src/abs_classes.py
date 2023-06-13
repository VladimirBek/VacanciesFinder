from abc import ABC, abstractmethod


class API(ABC):
    """
    Абстрактный класс для работы с API
    """

    @abstractmethod
    def get_vacancies(self, profession):
        """
        Абстрактный метод для получения объекта для работы с API
        """
        pass
