from abc import ABC, abstractmethod


class AbstractAPIJob(ABC):

    @abstractmethod
    def job_openings(self):
        pass