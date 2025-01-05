def contains_any_words(content: str, words: list) -> bool:
    """Функция для получения булевого значения, если хотя бы одно слово из списка words входит в передаваемый текст"""
    return any(word.lower() in content.lower() for word in words)


def get_top_n(data: list, top_n: int) -> list:
    """Функция сортировки списка по зарплате и вывода топа вакансий с самой большой зарплатой"""
    result = sorted(data, key=lambda x: (x["salary"]["from"], x["salary"]["to"]), reverse=True)
    return result[0:top_n]
