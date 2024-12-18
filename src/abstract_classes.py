from abc import ABC, abstractmethod


class AbstractAPIJob(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass