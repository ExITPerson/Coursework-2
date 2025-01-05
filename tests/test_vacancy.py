from src.vacancy import Vacancy


def test_filter_vacancies_positive(vacancies_for_the_filter: list) -> None:
    vacancies = Vacancy("Python", "url", "0-0")
    result = vacancies.filter_vacancies(vacancies_for_the_filter, "100000-150000", "Москва", 4, ["sql", "junior"])
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


def test_job_comparison() -> None:
    vacancy1 = Vacancy("Python Developer", "url1", "100000-150000")
    vacancy2 = Vacancy("Python Junior", "url2", "80000-120000")
    assert (vacancy1 < vacancy2) is False
    assert (vacancy2 < vacancy1) is True
