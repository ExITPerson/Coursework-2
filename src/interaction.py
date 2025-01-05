from src.file_saver import CSVSaver, ExcelSaver, JsonSaver, TXTSaver
from src.job_opening import HeadHunterAPI
from src.utils import get_top_n
from src.vacancy import Vacancy


def user_interaction() -> None:
    """Функция взаимодействия с пользователем"""
    search_query = input("Введите поисковый запрос: ")

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    filter_words = input(
        "Введите ключевые слова для фильтрации вакансий через запятую (Например: Junior, Developer): "
    ).split(", ")
    salary_range = input("Введите диапазон зарплат по шаблону (100000-200000): ")
    experience = int(input("Введите стаж работы по искомой профессии (в годах): "))
    city = input("Введите город для поиска работы: ")

    search = HeadHunterAPI().get_vacancies(search_query)

    vacancies = Vacancy("Python", "https://hh.ru/vacancy/112770759", "100000-200000")
    search_result = vacancies.filter_vacancies(search, salary_range, city, experience, filter_words)

    result = get_top_n(search_result, top_n)

    json_saver = JsonSaver
    json_saver.save_data(result, "user_search")

    csv_saver = CSVSaver
    csv_saver.save_data(result, "user_search")

    excel_saver = ExcelSaver
    excel_saver.save_data(result, "user_search")

    txt_saver = TXTSaver
    txt_saver.save_data(result, "user_search")

    print(f"Топ-{top_n} вакансий по вашему запросу:")

    for vacancy in result:
        if vacancy["experience"]["name"] == "0":
            vacancy["experience"]["name"] = "Без опыта"
        if vacancy["salary"]["to"] == 0:
            print(
                f"\nНазвание вакансии: {vacancy["name"]}\n"
                f"URL: {vacancy["alternate_url"]}\n"
                f"Зарплата: От {vacancy["salary"]["from"]}\n"
                f"Опыт работы: {vacancy["experience"]["name"]}\n"
            )
        else:
            print(
                f"\nНазвание вакансии: {vacancy["name"]}\n"
                f"URL: {vacancy["alternate_url"]}\n"
                f"Зарплата: От {vacancy["salary"]["from"]} до {vacancy["salary"]["to"]}\n"
                f"Опыт работы: {vacancy["experience"]["name"]}\n"
            )
            print(JsonSaver.get_data("data", "user_search"))
