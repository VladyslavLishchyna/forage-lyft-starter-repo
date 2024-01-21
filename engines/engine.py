from datetime import datetime
from abstract.serviceable import Serviceable
from engines.service_needed_checkers.abstract.abstract_engine_service_needed_checker import AbstractEngineServiceNeededChecker


class Engine(Serviceable):
    def __init__(self, current_mileage: int, last_service_mileage: int, warning_light_on: bool,
                 last_service_date: datetime, service_needed_checker: AbstractEngineServiceNeededChecker):
        super().__init__(self, last_service_date)

        self.current_mileage = current_mileage
        self.warning_light_on = warning_light_on
        self.last_service_mileage = last_service_mileage
        self.service_needed_checker = service_needed_checker
        self.mileage_after_last_service = self.current_mileage - self.last_service_mileage