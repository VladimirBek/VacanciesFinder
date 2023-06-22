import json

from src.abs_classes import FileMaker


class JsonSaver(FileMaker):

    def __init__(self):
        """При инициализации класса, появляется файл, содержащий пустой список"""
        with open('Vacancies_info.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps([], indent=2, ensure_ascii=False))

    def get_info(self) -> list:
        """
        Метод для получения вакансий из файла в формате list
        :return: Список вакансий
        """
        with open('Vacancies_info.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def add_vacancy(self, vacancy):
        """
        Метод для дополнения вакансии файл
        :param vacancy: экземпляр класса Vacancy
        :return: None. Вакансии записываются в файл.
        """
        data = vacancy.__dict__
        lst = json.load(open('Vacancies_info.json'))
        lst.append(data)
        with open('Vacancies_info.json', 'w', encoding='utf-8') as file:
            json.dump(lst, file, indent=2, ensure_ascii=False)

    def del_vacancy(self, id: str):
        """
        Метод для удаления вакансии из файла.
        :param id: ID вакансии, которую нужно удалить из файла
        :return: None. Создается новый файл, в котором выбранная вакансия отсутствует.
        """
        with open('Vacancies_info.json', 'r+', encoding='utf-8') as file:
            data: list = json.load(file)
        for vac in data:
            if id == vac['id']:
                data.remove(vac)
        with open('Vacancies_info.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def sort_data(self, key: int):
        """
        Метод для сортировки вакансий по указанному ключу
        :param key: ключ для сортировки
        :return: None. Вакансии сортируются в файле. После выполнения метода, файл перезаписывается.
        """
        with open('Vacancies_info.json', 'r+', encoding='utf-8') as file:
            data = json.load(file)
        if key == 2:
            data = sorted(data, key=lambda dic: (dic['salary_from'] + dic['salary_to']) / 2, reverse=True)
            with open('Vacancies_info.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        elif key == 1:
            data = sorted(data, key=lambda dic: dic['title'])
            with open('Vacancies_info.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        else:
            return 'Невозможно отсортировать вакансии по данному ключу'

    def filter_by_area(self, area) -> list:
        """
        Метод для фильтрации вакансий по городу
        :param area: город для фильтрации
        :return: отфильтрованный по городу список вакансий
        """
        with open('Vacancies_info.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return [vac for vac in data if vac['area'] == area]

    def filter_by_salary(self, start=0, to=0) -> list:
        """
        Метод для фильтрации вакансий по зарплате
        :param start: минимальное значение з/п (default=0)
        :param to: максимальное значение з/п (default=0)
        :return: отфильтрованный по зарплате список вакансий
        """
        with open('Vacancies_info.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        if to == 0:
            return list(filter(lambda dic: dic['salary_from'] >= start, data))
        return list(filter(lambda dic: dic['salary_from'] >= start and dic['salary_to'] <= to, data))
