from abc import ABC, abstractmethod


class AbstractEngineServiceNeededChecker(ABC): 
    @abstractmethod
    def needs_service(self) -> bool:
        pass