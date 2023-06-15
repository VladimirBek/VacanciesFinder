from src.sj_api import SuperJobAPI


def test_get_vacancies():
    sj_api = SuperJobAPI()
    assert isinstance(sj_api.get_vacancies('HR'), list)
