class Vacancy:
    vacancies_list = []

    def __init__(self, salary: str, area: str, employment: str, experience: int) -> None:
        self.salary = salary
        self.area = area
        self.employment = employment
        self.experience = experience
        self.vacancies_list = []

    @classmethod
    def cast_to_object_list(cls, vacancies):
        cls.vacancies_list = []
        for vacancy in vacancies["items"]:
            cls.vacancies_list.append(vacancy)
        return cls.vacancies_list



