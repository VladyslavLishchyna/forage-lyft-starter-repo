from abc import ABC, abstractmethod

from engines.service_needed_checkers.abstract.engine_interface import IEngine


class AbstractEngineServiceNeededChecker(ABC):
    @abstractmethod
    def needs_service(self, engine: IEngine) -> bool:
        pass
