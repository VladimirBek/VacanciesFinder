from src.hh_api import HeadHunterAPI


def test_get_vacancies():
    hh_api = HeadHunterAPI()
    assert isinstance(hh_api.get_vacancies('HR помощник'), list)
