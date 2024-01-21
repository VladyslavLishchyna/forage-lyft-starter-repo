import unittest
from datetime import datetime, timedelta

from batteries.batteries_service_needed_checker import BatteriesServiceNeededChecker
from batteries.battery import Battery


class BatteryTests(unittest.TestCase):
    TIME_BETWEEN_SERVICES = timedelta(weeks=50)
    SERVICE_NEEDED_CHECKER = BatteriesServiceNeededChecker(TIME_BETWEEN_SERVICES)

    def test_battery_needed_service_happy_case(self):
        # Arrange
        last_service_date = datetime.today() - self.TIME_BETWEEN_SERVICES - timedelta(minutes=5)
        battery = Battery(last_service_date, self.SERVICE_NEEDED_CHECKER)
        # Act
        # Assert
        self.assertTrue(battery.needs_service())

    def test_battery_dont_need_service_happy_case(self):
        # Arrange
        last_service_date = datetime.today() - self.TIME_BETWEEN_SERVICES + timedelta(minutes=5)
        battery = Battery(last_service_date, self.SERVICE_NEEDED_CHECKER)

        # Act
        # Assert
        self.assertFalse(battery.needs_service())
