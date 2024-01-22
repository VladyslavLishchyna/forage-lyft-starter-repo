from typing import List
from tires.service_needed_checkers.abstract.abstract_tires_service_needed_checker import \
    AbstractTiresServiceNeededChecker


class TiresServiceNeededCheckerBySingleTireWear(AbstractTiresServiceNeededChecker):
    def needs_service(self, tires_wear: List) -> bool:
        return any(x >= 0.9 for x in tires_wear)
