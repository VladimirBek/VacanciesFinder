from src.hh_api import HeadHunterAPI
from src.json_saver import JsonSaver
from src.sj_api import SuperJobAPI
from src.vacancy import Vacancy


def get_vacancies(platform: int = 3, profession='') -> list:
    """
    Метод для получения вакансий с конкретной платформы
    :param profession: Ключевое слово для поиска вакансий
    :param platform: Выбор платформы для поиска вакансий
    :return: список вакансий
    """

    if platform == 1:
        hh_api = HeadHunterAPI()
        hh_api.get_vacancies(profession)
        return Vacancy.vacancy_list
    elif platform == 2:
        sj_api = SuperJobAPI()
        sj_api.get_vacancies(profession)
        return Vacancy.vacancy_list
    else:
        hh_api = HeadHunterAPI()
        hh_api.get_vacancies(profession)
        sj_api = SuperJobAPI()
        sj_api.get_vacancies(profession)
        return Vacancy.vacancy_list


def show_info(vacancies: list) -> None:
    """
    Функция для вывода вакансий
    :param vacancies: Вакансии, которые надо вывести
    :return: None. В консоль выводятся вакансии в читабельном формате
    """
    print('Вот вакансии, которые нам удалось найти:\n')
    for vac in vacancies:
        if vac["salary_from"] == 0 and vac["salary_to"] != 0:
            print(f'ID вакансии: {vac["id"]}\n'
                  f'Организация: {vac["employer"]}\n'
                  f'Название вакансии: {vac["title"]}\n'
                  f'Зарплата: до {vac["salary_to"]} {vac["currency"]}\n'
                  f'Город: {vac["area"]}\n'
                  f'Ссылка на вакансию: {vac["url"]}'
                  f'\n')
        elif vac["salary_from"] != 0 and vac["salary_to"] == 0:
            print(f'ID вакансии: {vac["id"]}\n'
                  f'Организация: {vac["employer"]}\n'
                  f'Название вакансии: {vac["title"]}\n'
                  f'Зарплата: от {vac["salary_from"]} {vac["currency"]}\n'
                  f'Город: {vac["area"]}\n'
                  f'Ссылка на вакансию: {vac["url"]}'
                  f'\n')
        elif vac["salary_from"] != 0 and vac["salary_to"] != 0:
            print(f'ID вакансии: {vac["id"]}\n'
                  f'Организация: {vac["employer"]}\n'
                  f'Название вакансии: {vac["title"]}\n'
                  f'Зарплата: от {vac["salary_from"]} до {vac["salary_to"]} {vac["currency"]}\n'
                  f'Город: {vac["area"]}\n'
                  f'Ссылка на вакансию: {vac["url"]}'
                  f'\n')
        else:
            print(f'ID вакансии: {vac["id"]}\n'
                  f'Организация: {vac["employer"]}\n'
                  f'Название вакансии: {vac["title"]}\n'
                  f'Зарплата: {vac["currency"]}\n'
                  f'Город: {vac["area"]}\n'
                  f'Ссылка на вакансию: {vac["url"]}'
                  f'\n')


def user_interaction():
    """Функция работы программы и взаимодействия с пользователем"""

    print('Приветствую, пользователь в нашем сервисе по поиску вакансий!')
    try:
        choose_platform = int(input('Введите платформу, с которой хотите работать\n'
                                    '1 - Head Hunter\n'
                                    '2 - Super Job\n'
                                    '3 - Поиск со всех платформ\n'))
    except ValueError:
        print('Введено неверное значение. Введите целое число от 1 до 3')
        user_interaction()

    choose_profession = input('Введите название профессии для поиска вакансий:\n')
    vacancies = get_vacancies(choose_platform, choose_profession)
    if not vacancies:
        print('По Вашему запросу вакансий не найдено')
        return
    js = JsonSaver()
    for vac in vacancies:
        js.add_vacancy(vac)
    js.sort_data(1)
    vacancies = js.get_info()
    show_info(vacancies)
    while True:
        action = input('Выберите действие:\n'
                       '1 - Вывести вакансии еще раз\n'
                       '2 - Удалить вакансию из списка\n'
                       '3 - Отсортировать список вакансий по алфавиту или по зарплате\n'
                       '4 - Отфильтровать вакансии по городу или по зарплате\n'
                       '0 - Выйти из программы\n')
        if action == '1':
            vacancies = js.get_info()
            show_info(vacancies)
        elif action == '2':
            vac_id = input('Введите ID вакансии, которую хотите удалить из списка:\n')
            js.del_vacancy(vac_id)
            print('Выбранная вакансия удалена')
        elif action == '3':
            sort_by = input('Выберите признак для сортировки:\n'
                            '1 - Сортировка по алфавиту\n'
                            '2 - Сортировка по зарплате\n'
                            '0 - вернуться назад\n')
            if sort_by == '1':
                js.sort_data(1)
                print('Вакансии отсортированы по алфавиту')
                show_info(js.get_info())
            elif sort_by == '2':
                js.sort_data(2)
                print('Вакансии отсортированы по зарплате')
                show_info(js.get_info())
            elif sort_by == '0':
                pass
            else:
                print('Ошибка: нужно ввести значение 1 или 2')

        elif action == '4':
            filter_by = input('Выберите признак для фильтрации:\n'
                              '1 - Фильтрация по городу\n'
                              '2 - Фильтрация по зарплате\n'
                              '0 - вернуться назад\n')
            if filter_by == '1':
                city = input('Введите название города:\n')
                print('Ваши отфильтрованные по городу вакансии:\n')
                show_info(js.filter_by_area(city))
            elif filter_by == '2':
                try:
                    start = int(input('Введите минимальное значение зарплаты:\n'
                                      'Если минимальное значение не интересует, '
                                      'то введите произвольное значение или нажмите Enter\n'))
                except ValueError:
                    start = 0
                try:
                    to = int(input('Введите максимальное значение зарплаты:\n'
                                   'Если максимальное значение не интересует, '
                                   'то введите произвольное значение или нажмите Enter\n'))
                except ValueError:
                    to = 0
                show_info(js.filter_by_salary(start=start, to=to))
        elif action == '0':
            return
        else:
            print('Введено недопустимое значение')
