import pytest


@pytest.fixture
def vacancies() -> list:
    return [
        {"id": "1", "salary": None, "experience": {"name": "Нет опыта"}},
        {"id": "1", "salary": {"from": 10, "to": None}, "experience": {"name": "От 1 до 3 лет"}},
        {"id": "1", "salary": {"from": None, "to": 10}, "experience": {"name": "От 1 до 3 лет"}},
    ]


@pytest.fixture
def vacancies_for_the_filter() -> list:
    return [
        {
            "id": 1,
            "name": "Junior",
            "area": {"name": "Москва"},
            "salary": {"from": 100000, "to": 120000},
            "experience": {"name": "От 3 до 6"},
            "snippet": {"requirement": "sql", "responsibility": "Помощь"},
        },
        {
            "id": 2,
            "name": "Junior",
            "area": {"name": "Москва"},
            "salary": {"from": 90000, "to": 120000},
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
            "id": 4,
            "name": "Java",
            "area": {"name": "Москва"},
            "salary": {"from": 100000, "to": 120000},
            "experience": {"name": "От 3 до 6"},
            "snippet": {"requirement": "Разработка", "responsibility": "Помощь"},
        },
        {
            "id": 5,
            "name": "Junior",
            "area": {"name": "Москва"},
            "salary": {"from": 100000, "to": 160000},
            "experience": {"name": "От 3 до 6"},
            "snippet": {"requirement": "sql", "responsibility": "Помощь"},
        },
        {
            "id": 6,
            "name": "Junior",
            "area": {"name": "Ташкент"},
            "salary": {"from": 100000, "to": 120000},
            "experience": {"name": "От 3 до 6"},
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
