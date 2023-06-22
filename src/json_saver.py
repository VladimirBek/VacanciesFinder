import json

from src.abs_classes import FileMaker


class JsonSaver(FileMaker):

    def __init__(self):
        with open('Vacancies_info.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps([], indent=2, ensure_ascii=False))

    def get_info(self):
        with open('Vacancies_info.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def add_vacancy(self, vacancy):
        data = vacancy.__dict__
        lst = json.load(open('Vacancies_info.json'))
        lst.append(data)
        with open('Vacancies_info.json', 'w', encoding='utf-8') as file:
            json.dump(lst, file, indent=2, ensure_ascii=False)

    def del_vacancy(self, id: str):
        with open('Vacancies_info.json', 'r+', encoding='utf-8') as file:
            data: list = json.load(file)
        for vac in data:
            if id == vac['id']:
                data.remove(vac)
        with open('Vacancies_info.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def sort_data(self, key: int):
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

    def filter_by_area(self, area):
        with open('Vacancies_info.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return [vac for vac in data if vac['area'] == area]

    def filter_by_salary(self, start=0, to=0):
        """Метод для фильтрации вакансий по зарплате"""
        with open('Vacancies_info.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        if to == 0:
            return list(filter(lambda dic: dic['salary_from'] >= start, data))
        return list(filter(lambda dic: dic['salary_from'] >= start and dic['salary_to'] <= to, data))
