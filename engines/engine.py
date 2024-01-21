from datetime import datetime
from abstract.serviceable import Serviceable
from engines.service_needed_checkers.abstract.abstract_engine_service_needed_checker import \
    AbstractEngineServiceNeededChecker
from engines.service_needed_checkers.abstract.engine_interface import IEngine


class Engine(Serviceable, IEngine):
    def __init__(self, current_mileage: int, last_service_mileage: int, warning_light_on: bool,
                 last_service_date: datetime, service_needed_checker: AbstractEngineServiceNeededChecker):
        super().__init__(last_service_date)

        self._warning_light_on = warning_light_on
        self.service_needed_checker = service_needed_checker
        self._mileage_after_last_service = current_mileage - last_service_mileage

    def needs_service(self) -> bool:
        return self.service_needed_checker.needs_service(self)

    @property
    def warning_light_on(self):
        return self._warning_light_on

    @property
    def mileage_after_last_service(self):
        return self._mileage_after_last_service
