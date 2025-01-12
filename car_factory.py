from datetime import datetime

from batteries.battery import Battery
from batteries.battery_type import BatteryType
from car import Car
from engines.engine_type import EngineType
from engines.engines_factory import EnginesFactory
from batteries.batteries_factory import BatteriesFactory


class CarFactory:
    def __init__(self, engines_factory: EnginesFactory, batteries_factory: BatteriesFactory):
        self.engines_factory = engines_factory
        self.batteries_factory = batteries_factory

    def create(self, current_mileage: int, last_engine_service_mileage: int, warning_light_on: bool,
               engine_last_service_date: datetime, battery_last_service_date: datetime, engine_type: EngineType,
               battery_type: BatteryType):
        engine_service_needed_checking_type = self.engines_factory.engines_options.TYPE_OF_ENGINE_SERVICE_NEEDED_CHECK[engine_type]
        engine = self.engines_factory.create(current_mileage, last_engine_service_mileage, warning_light_on,
                                             engine_last_service_date, engine_type, engine_service_needed_checking_type)
        battery: Battery = self.batteries_factory.create(battery_last_service_date, battery_type)
        return Car(engine, battery)
