from datetime import timedelta
from datetime import datetime
from engines.engine import Engine
from engines.service_needed_checkers.abstract.abstract_engine_service_needed_checker import \
    AbstractEngineServiceNeededChecker as Checker


class EngineServiceNeededCheckerByMilleage(Checker):
    def __init__(self, number_of_miles_between_services: int):
        self.number_of_miles_between_services = number_of_miles_between_services

    def needs_service(self, engine: Engine) -> bool:
        return engine.mileage_after_last_service > self.number_of_miles_between_services
