from abc import ABC, abstractmethod
from datetime import datetime


class Serviceable(ABC):
    def __init__(self, last_service_date: datetime):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self) -> bool:
        pass
