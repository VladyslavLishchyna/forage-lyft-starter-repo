from typing import List
from tires.service_needed_checkers.abstract.abstract_tires_service_needed_checker import \
    AbstractTiresServiceNeededChecker


class TiresServiceNeededCheckerByTotalTiresWear(AbstractTiresServiceNeededChecker):
    def needs_service(self, tires_wear: List) -> bool:
        return sum(tires_wear) >= 3
