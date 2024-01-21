from engines.engine import Engine
from engines.service_needed_checkers.abstract.abstract_engine_service_needed_checker import \
    AbstractEngineServiceNeededChecker as Checker


class EngineServiceNeededCheckerByIndicator(Checker):
    def needs_service(self, engine: Engine) -> bool:
        return engine.warning_light_on
