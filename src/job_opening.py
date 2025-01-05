from typing import Any

import requests

from src.abstract_classes import AbstractAPIJob


class HeadHunterAPI(AbstractAPIJob):
    """Класс для получения информации о вакансиях из сервиса HH"""

    def __init__(self) -> None:
        """Инициализация"""
        # self.keyword = keyword
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies: list = []

    def __get_response(self) -> Any:
        """Функция для выполнения запроса к API"""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code == 200:
            return response.json()
        else:
            raise BaseException(f"Статус код: {response.status_code}")

    def get_vacancies(self, keyword: str) -> Any:
        """Функция получения данных о вакансиях через API"""
        self.__params["text"] = keyword
        initial_response = self.__get_response()
        total_pages = initial_response["pages"]

        while self.__params.get("page") < total_pages:
            self.__vacancies.extend(initial_response["items"])
            self.__params["page"] += 1

            if self.__params["page"] < total_pages:
                initial_response = self.__get_response()

        return self.__vacancies
