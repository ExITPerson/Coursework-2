from src.abstract_classes import AbstractAPIJob
import requests


class JobOpening(AbstractAPIJob):

    def job_openings(self):
        url = "https://api.hh.ru/vacancies"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()