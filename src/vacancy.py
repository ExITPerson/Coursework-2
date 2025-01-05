import re
from typing import Any

from src.utils import contains_any_words


class Vacancy:
    __slots__ = ["name", "url", "from_salary", "to_salary", "vacancies"]

    def __init__(self, name: str, url: str, salary: str) -> None:
        """Инициализация"""
        self.name = name
        self.url = url
        self.from_salary = int(salary.split("-")[0])
        self.to_salary = int(salary.split("-")[1])
        self.vacancies: list[Any] = []

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return (self.from_salary, self.to_salary) < (other.from_salary, other.to_salary)
        return NotImplemented

    @staticmethod
    def __get_custom_vacancies(vacancies: list) -> list:
        """Классметод для кастомизации получаемых данных в списке"""
        custom_vacancies = []
        if type(vacancies) is list:
            for vacancy in vacancies:
                if vacancy["salary"] is None:
                    vacancy["salary"] = {"from": 0, "to": 0}
                if vacancy["salary"]["to"] is None:
                    vacancy["salary"]["to"] = 0
                if vacancy["salary"]["from"] is None:
                    vacancy["salary"]["from"] = 0
                if vacancy["experience"]["name"] == "Нет опыта":
                    vacancy["experience"]["name"] = "0"
                custom_vacancies.append(vacancy)
            return custom_vacancies
        else:
            raise TypeError(f"Передаваемый тип данных: {type(vacancies)}.")

    def filter_vacancies(self, vacancies: list, salary: str, area: str, experience: int, keywords: list) -> list:
        """Функция фильтрации получаемых данных из списка, для отбора вакансий по заданным параметрам"""
        custom_vacancies = self.__get_custom_vacancies(vacancies)
        from_salary = int(salary.split("-")[0])
        to_salary = int(salary.split("-")[1])
        for vacancy in custom_vacancies:
            requirement = str(vacancy["snippet"]["requirement"]).lower()
            responsibility = str(vacancy["snippet"]["responsibility"]).lower()
            name = str(vacancy["name"]).lower()
            if (
                from_salary <= vacancy["salary"]["from"] <= to_salary
                and from_salary <= vacancy["salary"]["to"] <= to_salary
            ):
                if area.lower() in vacancy["area"]["name"].lower():
                    if experience >= int(re.findall(r"\d", vacancy["experience"]["name"])[0]):
                        if (
                            contains_any_words(requirement, keywords)
                            or contains_any_words(responsibility, keywords)
                            or contains_any_words(name, keywords)
                        ):
                            self.vacancies.append(vacancy)
        return self.vacancies
