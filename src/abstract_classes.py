from abc import ABC, abstractmethod


class AbstractAPIJob(ABC):

    @abstractmethod
    def get_vacancies(self) -> None:
        pass


class AbstractSaveFile(ABC):

    @abstractmethod
    def save_data(self, data: list, file_name: str) -> None:
        pass

    @abstractmethod
    def del_data(self, data: list, file_name: str) -> None:
        pass
