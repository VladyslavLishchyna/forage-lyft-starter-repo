from datetime import datetime

from abstract.serviceable import Serviceable
from batteries.batteries_service_needed_checker import BatteriesServiceNeededChecker


class Battery(Serviceable):
    def __init__(self, last_service_date: datetime, service_needed_checker: BatteriesServiceNeededChecker):
        super().__init__(last_service_date)
        self.service_needed_checker = service_needed_checker

    def needs_service(self) -> bool:
        return self.service_needed_checker.needs_service(self.last_service_date)
