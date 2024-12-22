from src.utils import contains_any_words, content_id


def test_contains_any_word_true():
    content = "Привет, Ваня"
    words = ["Саша","Ваня", "Лиза"]
    assert contains_any_words(content, words) == True

def test_contains_any_word_false():
    content = "Привет, Света"
    words = ["Саша","Ваня", "Лиза"]
    assert contains_any_words(content, words) == False

def test_content_id_true():
    data = [{"id": "1"}, {"id": "2"}]
    content = "2"
    assert content_id(data, content) == True

def test_content_id_false():
    data = [{"id": "1"}, {"id": "2"}]
    content = "3"
    assert content_id(data, content) == False