from src.job_opening import HeadHunterAPI
from src.data_filtering import Vacancy


if __name__ == "__main__":
    response = HeadHunterAPI()
    hh_vacancies = response.get_vacancies("Python")

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    print(vacancies_list)

