from src.hh_api import HeadHunterAPI
from src.sj_api import SuperJobAPI


def get_vacancies(platform: int = 3) -> list:
    """
    Метод для получения вакансий с конкретной платформы
    :param platform: Выбор платформы для поиска вакансий
    :return: список вакансий
    """
    user_input = input('Введите название вакансии:\n')

    if platform == 1:
        hh_api = HeadHunterAPI()
        hh_vacancies = hh_api.get_vacancies(user_input)
        return hh_vacancies
    elif platform == 2:
        sj_api = SuperJobAPI()
        sj_vacancies = sj_api.get_vacancies(user_input)
        return sj_vacancies
    else:
        hh_api = HeadHunterAPI()
        hh_vacancies = hh_api.get_vacancies(user_input)
        sj_api = SuperJobAPI()
        sj_vacancies = sj_api.get_vacancies(user_input)
        hh_vacancies.extend(sj_vacancies)
        return hh_vacancies
