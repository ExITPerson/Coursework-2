from abc import ABC, abstractmethod


class AbstractAPIJob(ABC):
    """Абстрактный метод для работы с API"""

    @abstractmethod
    def get_vacancies(self, keyword: str) -> None:
        pass


class AbstractSaveFile(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def save_data(self, data: list, file_name: str) -> None:
        pass

    @abstractmethod
    def del_data(self, data: list, file_name: str) -> None:
        pass
