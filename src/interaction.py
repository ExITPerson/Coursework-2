from src.job_opening import HeadHunterAPI
from src.utils import get_top_n
from src.vacancy import Vacancy


def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    search = HeadHunterAPI(search_query).get_vacancies()
    top_n = input("Введите количество вакансий для вывода в топ N: ")

    filter_words = input("Введите ключевые слова для фильтрации вакансий через запятую (Например: Junior, Developer): ").split(", ")
    salary_range = input("Введите диапазон зарплат по шаблону (100000-200000): ")
    experience = int(input("Введите стаж работы по искомой профессии (в годах): "))
    city = input("Введите город для поиска работы: ")

    vacancies = Vacancy(salary_range, city, experience, filter_words)
    custom = vacancies.custom(search)
    search_result = vacancies.filter_vacancies()

    result = get_top_n(search_result, top_n)

    print(f"Топ-{top_n} вакансий по вашему запросу:")

    for vacancy in result:
        print(
            f"Название вакансии: {vacancy["name"]}"
            f"URL: {vacancy["branding"]["alternate_url"]}"
            f"Зарплата: От {vacancy["salary"]["from"]} до {vacancy["salary"]["to"]}"
            f"Опыт работы: {vacancy["experience"]["name"]}"
        )
