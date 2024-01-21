from datetime import datetime
import unittest

from engines.engine import Engine
from engines.service_needed_checkers.implementations.engine_service_needed_checker_by_indicator import \
    EngineServiceNeededCheckerByIndicator
from engines.service_needed_checkers.implementations.engine_service_needed_checker_by_milleage import \
    EngineServiceNeededCheckerByMilleage


class EngineTests(unittest.TestCase):
    LAST_SERVICE_MILLEAGE = 9000
    MILLEAGE_BETWEEN_SERVICES = 5000
    LAST_SERVICE_DATE = datetime.today()
    SERVICE_NEEDED_CHECKER_BY_INDICATOR = EngineServiceNeededCheckerByIndicator()
    SERVICE_NEEDED_CHECKER_BY_MILLEAGE = EngineServiceNeededCheckerByMilleage(MILLEAGE_BETWEEN_SERVICES)

    def test_engine_needed_service_by_milleage_happy_case(self):
        # Arrange
        current_milleage = self.LAST_SERVICE_MILLEAGE + self.MILLEAGE_BETWEEN_SERVICES + 5
        engine = Engine(current_milleage, self.LAST_SERVICE_MILLEAGE, False, self.LAST_SERVICE_DATE, self.SERVICE_NEEDED_CHECKER_BY_MILLEAGE)
        # Act
        # Assert
        self.assertTrue(engine.needs_service())

    def test_engine_dont_needed_service_by_milleage_happy_case(self):
        # Arrange
        current_milleage = self.LAST_SERVICE_MILLEAGE + self.MILLEAGE_BETWEEN_SERVICES - 5
        engine = Engine(current_milleage, self.LAST_SERVICE_MILLEAGE, False, self.LAST_SERVICE_DATE, self.SERVICE_NEEDED_CHECKER_BY_MILLEAGE)
        # Act
        # Assert
        self.assertFalse(engine.needs_service())

    def test_engine_needed_service_by_indicator_happy_case(self):
        # Arrange
        engine = Engine(self.LAST_SERVICE_MILLEAGE, self.LAST_SERVICE_MILLEAGE, True, self.LAST_SERVICE_DATE, self.SERVICE_NEEDED_CHECKER_BY_INDICATOR)
        # Act
        # Assert
        self.assertTrue(engine.needs_service())

    def test_engine_dont_needed_service_by_indicator_happy_case(self):
        # Arrange
        engine = Engine(self.LAST_SERVICE_MILLEAGE, self.LAST_SERVICE_MILLEAGE, False, self.LAST_SERVICE_DATE, self.SERVICE_NEEDED_CHECKER_BY_INDICATOR)
        # Act
        # Assert
        self.assertFalse(engine.needs_service())
