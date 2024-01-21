from abc import ABC, abstractmethod


class IEngine(ABC):
    @property
    @abstractmethod
    def warning_light_on(self) -> bool:
        pass

    @property
    @abstractmethod
    def mileage_after_last_service(self) -> int:
        pass
