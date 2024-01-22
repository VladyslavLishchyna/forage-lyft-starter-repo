from abc import ABC, abstractmethod
from typing import List


class AbstractTiresServiceNeededChecker(ABC):
    @abstractmethod
    def needs_service(self, tires_wear: List) -> bool:
        pass
