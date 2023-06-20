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


class FileMaker(ABC):
    """
    Абстрактный метод для работы с файлами JSON формата
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        """Метод для добавления вакансии в файл"""
        pass

    @abstractmethod
    def del_vacancy(self, id):
        """Метод для удаления вакансии из файла"""
        pass

    @abstractmethod
    def sort_data(self, key):
        """ Метод для сортировки вакансий"""
        pass

    @abstractmethod
    def filter_by_area(self, area):
        """Метод для фильтрации вакансий по городу"""
        pass

    @abstractmethod
    def filter_by_salary(self, start, to):
        """Метод для фильтрации вакансий по городу"""
        pass
