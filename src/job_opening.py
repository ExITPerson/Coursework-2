from src.abstract_classes import AbstractAPIJob
import requests


class HeadHunterAPI(AbstractAPIJob):
    def __init__(self, keyword):
        self.keyword = keyword
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {"text": "", 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_vacancies(self) -> list:
        self.params["text"] = self.keyword
        while self.params.get("page") != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)

            if response.status_code == 200:
                vacancies = response.json()["items"]
                self.vacancies.extend(vacancies)
                self.params['page'] += 1
            else:
                raise BaseException(f"Статус код: {response.status_code}")
        return self.vacancies
