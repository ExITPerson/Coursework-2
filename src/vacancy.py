import re
from src.utils import contains_any_words

class Vacancy:
    vacancies: list[dict]
    custom_vacancies = []

    def __init__(self, salary, area, experience, keywords):
        self.from_salary = int(salary.split("-")[0])
        self.to_salary = int(salary.split("-")[1])
        self.area = area.lower()
        self.experience = experience
        self.keywords = keywords
        self.vacancies = []

    @classmethod
    def custom(cls, vacancies):
        for vacancy in vacancies:
            if vacancy["salary"] is None:
                vacancy["salary"] = {"from": 0, "to": 0}
            if vacancy["salary"]["to"] is None:
                vacancy["salary"]["to"] = 0
            if vacancy["salary"]["from"] is None:
                vacancy["salary"]["from"] = 0
            if vacancy["experience"]["name"] == "Нет опыта":
                vacancy["experience"]["name"] = "0"
            cls.custom_vacancies.append(vacancy)
        return cls.custom_vacancies

    def filter_vacancies(self):
        for vacancy in Vacancy.custom_vacancies:
            requirement = str(vacancy["snippet"]["requirement"]).lower()
            responsibility = str(vacancy["snippet"]["responsibility"]).lower()
            name = str(vacancy["name"]).lower()
            if (self.from_salary <= vacancy["salary"]["from"] <= self.to_salary
                    and self.from_salary <= vacancy["salary"]["to"] <= self.to_salary):
                if self.area in vacancy["area"]["name"].lower():
                    if self.experience >= int(re.findall(r"\d", vacancy["experience"]["name"])[0]):
                        if (contains_any_words(requirement, self.keywords)
                            or contains_any_words(responsibility, self.keywords)
                            or contains_any_words(name, self.keywords)):
                            self.vacancies.append(vacancy)
        return self.vacancies

