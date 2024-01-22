from datetime import datetime
from typing import List

from abstract.serviceable import Serviceable
from tires.service_needed_checkers.abstract.abstract_tires_service_needed_checker import \
    AbstractTiresServiceNeededChecker


class Tires(Serviceable):
    def __init__(self, last_service_date: datetime, tires_wear: List, service_needed_checker: AbstractTiresServiceNeededChecker):
        super().__init__(last_service_date)
        self.tires_wear = tires_wear
        self.service_needed_checker = service_needed_checker

    def needs_service(self) -> bool:
        return self.service_needed_checker.needs_service(self.tires_wear)
