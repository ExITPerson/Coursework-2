from src.file_saver import JsonSaver
from src.job_opening import HeadHunterAPI
import json

from src.vacancy import Vacancy

if __name__ == "__main__":
    hh_vacancies = HeadHunterAPI("Python").get_vacancies()
    #print(hh_vacancies)

    job_search = Vacancy("100000-130000", "Москва", 4, ["sql", "junior"])
    vacancy = job_search.custom(hh_vacancies)

    vacancy1 = job_search.filter_vacancies()
    # for vacancy in vacancy1:
    #     print(vacancy["id"])

    JsonSaver().save_data(vacancy1, "vacancies")



