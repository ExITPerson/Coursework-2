from typing import Any

import requests

from src.abstract_classes import AbstractAPIJob


class HeadHunterAPI(AbstractAPIJob):
    def __init__(self, keyword: str) -> None:
        self.keyword = keyword
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies: list = []
        self.data: int = 0

    def get_vacancies(self) -> list:
        self.params["text"] = self.keyword
        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code == 200:
            total_pages = response.json()["pages"]
        else:
            raise BaseException(f"Статус код: {response.status_code}")

        while self.params.get("page") != total_pages:
            response = requests.get(self.url, headers=self.headers, params=self.params)

            if response.status_code == 200:
                vacancies = response.json()["items"]
                self.vacancies.extend(vacancies)
                self.params["page"] += 1
            else:
                raise BaseException(f"Статус код: {response.status_code}")

        return self.vacancies
