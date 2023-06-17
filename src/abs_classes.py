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


class JSON(ABC):
    """
    Абстрактный метод для работы с файлами JSON формата
    """

    @abstractmethod
    def add_vacancy(self, id):
        """Метод для добавления вакансии в файл"""
        pass

    @abstractmethod
    def del_vacancy(self, id):
        """Метод для удаления вакансии из файла"""
        pass

    @abstractmethod
    def get_formate_vacancies(self, id):
        """Метод для получения вакансий из файла в формате типа Vacancy"""
        pass
