import pandas as pd

from src.abstract_classes import AbstractAPIJob
import requests


class HeadHunterAPI(AbstractAPIJob):

    def get_vacancies(self, name=None) -> pd.DataFrame:
        url = "https://api.hh.ru/vacancies"
        params = {"text": name}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise BaseException(f"Статус код: {response.status_code}")