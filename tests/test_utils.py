from src.utils import contains_any_words, get_top_n


def test_contains_any_word_true() -> None:
    content = "Привет, Ваня"
    words = ["Саша", "Ваня", "Лиза"]
    assert contains_any_words(content, words) is True


def test_contains_any_word_false() -> None:
    content = "Привет, Света"
    words = ["Саша", "Ваня", "Лиза"]
    assert contains_any_words(content, words) is False


def test_get_top_n() -> None:
    salary = [
        {"salary": {"from": 100000, "to": 130000}},
        {"salary": {"from": 50000, "to": 80000}},
        {"salary": {"from": 140000, "to": 180000}},
    ]
    result = get_top_n(salary, 2)
    print(result)
    assert result == [{"salary": {"from": 140000, "to": 180000}}, {"salary": {"from": 100000, "to": 130000}}]


def test_get_top_n_one_dict() -> None:
    salary = [{"salary": {"from": 100000, "to": 130000}}]
    result = get_top_n(salary, 4)
    print(result)
    assert result == [{"salary": {"from": 100000, "to": 130000}}]
