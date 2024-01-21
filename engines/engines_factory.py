from datetime import datetime
from engines.engine import Engine
from engines.engine_type import EngineType
from engines.engines_options import EnginesOptions
from engines.service_needed_checkers.engine_service_needed_checking_type import EngineServiceNeededCheckingType
from engines.service_needed_checkers.implementations.engine_service_needed_checker_by_indicator import EngineServiceNeededCheckerByIndicator
from engines.service_needed_checkers.implementations.engine_service_needed_checker_by_milleage import EngineServiceNeededCheckerByMilleage


class EnginesFactory():
    def __init__(self, engines_options: EnginesOptions):
        self.engines_options = engines_options

    def create(self, current_mileage: int, last_service_mileage: int, warning_light_on: bool,
                 last_service_date: datetime, engine_type: EngineType, engine_service_needed_checking_type: EngineServiceNeededCheckingType):
        
        engine_service_needed_checker = self.__resolve_engine_service_needed_checker(engine_type, engine_service_needed_checking_type)
        return Engine(current_mileage, last_service_mileage, warning_light_on, last_service_date, engine_service_needed_checker)
    
    def __resolve_engine_service_needed_checker(self, engine_type: EngineType, engine_service_needed_checking_type: EngineServiceNeededCheckingType):
        match engine_service_needed_checking_type:
            case EngineServiceNeededCheckingType.BY_INDICATOR:
                return EngineServiceNeededCheckerByIndicator()
            case EngineServiceNeededCheckingType.BY_MILLEAGE:
                milleage_between_services = self.engines_options.MILLEAGE_BETWEEN_SERVICES[engine_type]
                return EngineServiceNeededCheckerByMilleage(milleage_between_services)
            case _:
                raise("Can`t resolve EngineServiceNeededChecker")