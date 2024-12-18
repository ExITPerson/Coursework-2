from src.abstract_classes import AbstractAPIJob
import requests


class JobOpening(AbstractAPIJob):

    def job_openings(self):
        url = "https://api.hh.ru/vacancies"
        params = {"period": 90}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise BaseException(f"Статус код: {response.status_code}")