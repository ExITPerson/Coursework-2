import pytest

from src.vacancy import Vacancy


def test_custom_positive(vacancies: list) -> None:
    hh_vacancies = Vacancy("100000-150000", "Москва", 4, ["sql", "junior"])
    vacancy = hh_vacancies.custom(vacancies)
    print(vacancy)
    assert vacancy == [
        {"id": "1", "salary": {"from": 0, "to": 0}, "experience": {"name": "0"}},
        {"id": "1", "salary": {"from": 10, "to": 0}, "experience": {"name": "От 1 до 3 лет"}},
        {"id": "1", "salary": {"from": 0, "to": 10}, "experience": {"name": "От 1 до 3 лет"}},
    ]
    Vacancy.custom_vacancies = []


def test_custom_negative() -> None:
    hh_vacancies = Vacancy("100000-150000", "Москва", 4, ["sql", "junior"])
    with pytest.raises(TypeError, match="Передаваемый тип данных: <class 'dict'>."):
        hh_vacancies.custom({})
    Vacancy.custom_vacancies = []


def test_custom_empty_list() -> None:
    hh_vacancies = Vacancy("100000-150000", "Москва", 4, ["sql", "junior"])
    result = hh_vacancies.custom([])
    print(result)
    assert result == []
    Vacancy.custom_vacancies = []


def test_filter_vacancies_positive(vacancies_for_the_filter: list) -> None:
    vacancies = Vacancy("100000-150000", "Москва", 4, ["sql", "junior"])
    vacancies.custom(vacancies_for_the_filter)
    result = vacancies.filter_vacancies()
    assert result == [
        {
            "id": 1,
            "name": "Junior",
            "area": {"name": "Москва"},
            "salary": {"from": 100000, "to": 120000},
            "experience": {"name": "От 3 до 6"},
            "snippet": {"requirement": "sql", "responsibility": "Помощь"},
        },
        {
            "id": 3,
            "name": "Junior",
            "area": {"name": "Москва"},
            "salary": {"from": 100000, "to": 120000},
            "experience": {"name": "От 1 до 3"},
            "snippet": {"requirement": "sql", "responsibility": "Помощь"},
        },
        {
            "id": 7,
            "name": "Junior",
            "area": {"name": "Москва"},
            "salary": {"from": 100000, "to": 120000},
            "experience": {"name": "От 3 до 6"},
            "snippet": {"requirement": "Помощь", "responsibility": "sql"},
        },
    ]
    Vacancy.custom_vacancies = []
