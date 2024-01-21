from datetime import datetime

from batteries.batteries_options import BatteriesOptions
from batteries.batteries_service_needed_checker import BatteriesServiceNeededChecker
from batteries.battery import Battery
from batteries.battery import BatteryType


class BatteriesFactory():
    def __init__(self, batteries_options: BatteriesOptions):
        self.batteries_service_needed_checkers = {}

        for specific_battery_type in BatteryType:
            period_between_services = batteries_options.PERRIOD_BETWEEN_SERVICES[specific_battery_type]
            self.batteries_service_needed_checkers[specific_battery_type] = BatteriesServiceNeededChecker(period_between_services)

    def create(self, last_service_date: datetime, battery_type: BatteryType):
        service_needed_checker = self.batteries_service_needed_checkers[battery_type]
        return Battery(last_service_date,service_needed_checker)
