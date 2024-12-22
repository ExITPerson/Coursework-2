from abc import ABC, abstractmethod


class AbstractAPIJob(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class AbstractSaveFile(ABC):

    @abstractmethod
    def save_data(self, data, file_name):
        pass

    @abstractmethod
    def del_data(self, data, file_name):
        pass