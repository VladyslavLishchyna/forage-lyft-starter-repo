import unittest
from datetime import datetime, timedelta

from batteries.batteries_factory import BatteriesFactory
from batteries.batteries_options import BatteriesOptions
from batteries.battery_type import BatteryType
from car import Car
from car_factory import CarFactory
from engines.engine_type import EngineType
from engines.engines_factory import EnginesFactory
from engines.engines_options import EnginesOptions


class CarTests(unittest.TestCase):
    # Calliope - Capulet engine, Spindler battery
    # Glissade - Wiloughby engine, Spindler battery
    # Palindrome - Sternman engine, Spindler battery indicator!
    # Roschach - Wiloughby engine, Nubbin battery
    # Thovex - Capulet engine, Nubbin battery
    LAST_ENGINE_SERVICE_MILLEAGE = 9000
    CURRENT_DATE = datetime.today()

    ENGINE_OPTIONS = EnginesOptions()
    BATTERIES_OPTIONS = BatteriesOptions()
    ENGINE_FACTORY = EnginesFactory(ENGINE_OPTIONS)
    BATTERIES_FACTORY = BatteriesFactory(BATTERIES_OPTIONS)
    CAR_FACTORY = CarFactory(ENGINE_FACTORY, BATTERIES_FACTORY)

    THOVEX_CAR = (EngineType.CAPULET, BatteryType.NUBBIN)
    CALLIOPE_CAR = (EngineType.CAPULET, BatteryType.SPINDLER)
    ROSCHACH_CAR = (EngineType.WILLOUGHBY, BatteryType.NUBBIN)
    GLISSADE_CAR = (EngineType.WILLOUGHBY, BatteryType.SPINDLER)
    PALINDROME_CAR = (EngineType.STERNMAN, BatteryType.SPINDLER)

    def test_calliope_dont_need_service_happy_case(self):
        self._generic_test_car_dont_need_service_happy_case(self.CALLIOPE_CAR)

    def test_calliope_engine_indicator_turn_on(self):
        self._generi_test_engine_indicator_turn_on(self.CALLIOPE_CAR, False)

    def test_calliope_have_to_match_miles_after_service(self):
        self._generic_test_car_have_to_match_miles_after_service(self.CALLIOPE_CAR, True)

    def test_calliope_have_to_huge_time_without_battery_service(self):
        self._generic_test_car_have_to_huge_time_without_battery_service(self.CALLIOPE_CAR, True)

    def test_calliope_have_to_huge_time_without_engine_service(self):
        self._generic_test_car_have_to_huge_time_without_engine_service(self.CALLIOPE_CAR, False)

    def test_glissade_dont_need_service_happy_case(self):
        self._generic_test_car_dont_need_service_happy_case(self.GLISSADE_CAR)

    def test_glissade_engine_indicator_turn_on(self):
        self._generi_test_engine_indicator_turn_on(self.GLISSADE_CAR, False)

    def test_glissade_have_to_match_miles_after_service(self):
        self._generic_test_car_have_to_match_miles_after_service(self.GLISSADE_CAR, True)

    def test_glissade_have_to_huge_time_without_battery_service(self):
        self._generic_test_car_have_to_huge_time_without_battery_service(self.GLISSADE_CAR, True)

    def test_glissade_have_to_huge_time_without_engine_service(self):
        self._generic_test_car_have_to_huge_time_without_engine_service(self.GLISSADE_CAR, False)

    def test_palindrome_dont_need_service_happy_case(self):
        self._generic_test_car_dont_need_service_happy_case(self.PALINDROME_CAR)

    def test_palindrome_engine_indicator_turn_on(self):
        self._generi_test_engine_indicator_turn_on(self.PALINDROME_CAR, True)

    def test_palindrome_have_to_match_miles_after_service(self):
        self._generic_test_car_have_to_match_miles_after_service(self.PALINDROME_CAR, False)

    def test_palindrome_have_to_huge_time_without_battery_service(self):
        self._generic_test_car_have_to_huge_time_without_battery_service(self.PALINDROME_CAR, True)

    def test_palindrome_have_to_huge_time_without_engine_service(self):
        self._generic_test_car_have_to_huge_time_without_engine_service(self.PALINDROME_CAR, False)

    def test_roschach_dont_need_service_happy_case(self):
        self._generic_test_car_dont_need_service_happy_case(self.ROSCHACH_CAR)

    def test_roschach_engine_indicator_turn_on(self):
        self._generi_test_engine_indicator_turn_on(self.ROSCHACH_CAR, False)

    def test_roschach_have_to_match_miles_after_service(self):
        self._generic_test_car_have_to_match_miles_after_service(self.ROSCHACH_CAR, True)

    def test_roschach_have_to_huge_time_without_battery_service(self):
        self._generic_test_car_have_to_huge_time_without_battery_service(self.ROSCHACH_CAR, True)

    def test_roschach_have_to_huge_time_without_engine_service(self):
        self._generic_test_car_have_to_huge_time_without_engine_service(self.ROSCHACH_CAR, False)

    def test_thovex_dont_need_service_happy_case(self):
        self._generic_test_car_dont_need_service_happy_case(self.THOVEX_CAR)

    def test_thovex_engine_indicator_turn_on(self):
        self._generi_test_engine_indicator_turn_on(self.THOVEX_CAR, False)

    def test_thovex_have_to_match_miles_after_service(self):
        self._generic_test_car_have_to_match_miles_after_service(self.THOVEX_CAR, True)

    def test_thovex_have_to_huge_time_without_battery_service(self):
        self._generic_test_car_have_to_huge_time_without_battery_service(self.THOVEX_CAR, True)

    def test_thovex_have_to_huge_time_without_engine_service(self):
        self._generic_test_car_have_to_huge_time_without_engine_service(self.THOVEX_CAR, False)

    def _generic_test_car_dont_need_service_happy_case(self, config):
        car = self._create_car_that_dont_need_service(config[0], config[1])
        self.assertFalse(car.needs_service())

    def _generi_test_engine_indicator_turn_on(self, config, test_result: bool):
        car = self._create_car_with_turn_on_warning_indicator(config[0], config[1])
        is_service_needed = car.needs_service()
        self.assertEqual(is_service_needed, test_result)

    def _generic_test_car_have_to_match_miles_after_service(self, config, test_result: bool):
        car = self._create_car_that_have_to_match_miles_after_service(config[0], config[1])
        is_service_needed = car.needs_service()
        self.assertEqual(is_service_needed, test_result)

    def _generic_test_car_have_to_huge_time_without_battery_service(self, config, test_result: bool):
        car = self._create_car_with_huge_time_without_battery_service(config[0], config[1])
        is_service_needed = car.needs_service()
        self.assertEqual(is_service_needed, test_result)

    def _generic_test_car_have_to_huge_time_without_engine_service(self, config, test_result: bool):
        car = self._create_car_with_huge_time_without_engine_service(config[0], config[1])
        is_service_needed = car.needs_service()
        self.assertEqual(is_service_needed, test_result)

    def _create_car_that_dont_need_service(self, engine_type: EngineType, battery_type: BatteryType) -> Car:
        milleage_between_services = self.ENGINE_OPTIONS.MILLEAGE_BETWEEN_SERVICES.get(engine_type)
        current_milleage = self.LAST_ENGINE_SERVICE_MILLEAGE + milleage_between_services - 5
        return self.CAR_FACTORY.create(current_milleage, self.LAST_ENGINE_SERVICE_MILLEAGE, False, self.CURRENT_DATE,
                                       self.CURRENT_DATE, engine_type, battery_type)

    def _create_car_that_have_to_match_miles_after_service(self, engine_type: EngineType, battery_type: BatteryType) -> Car:
        milleage_between_services = self.ENGINE_OPTIONS.MILLEAGE_BETWEEN_SERVICES.get(engine_type)
        current_milleage = self.LAST_ENGINE_SERVICE_MILLEAGE + milleage_between_services + 5
        return self.CAR_FACTORY.create(current_milleage, self.LAST_ENGINE_SERVICE_MILLEAGE, False, self.CURRENT_DATE,
                                       self.CURRENT_DATE, engine_type, battery_type)

    def _create_car_with_turn_on_warning_indicator(self, engine_type: EngineType, battery_type: BatteryType) -> Car:
        milleage_between_services = self.ENGINE_OPTIONS.MILLEAGE_BETWEEN_SERVICES.get(engine_type)
        current_milleage = self.LAST_ENGINE_SERVICE_MILLEAGE + milleage_between_services - 5
        return self.CAR_FACTORY.create(current_milleage, self.LAST_ENGINE_SERVICE_MILLEAGE, True, self.CURRENT_DATE,
                                       self.CURRENT_DATE, engine_type, battery_type)

    def _create_car_with_huge_time_without_battery_service(self, engine_type: EngineType, battery_type: BatteryType) -> Car:
        milleage_between_services = self.ENGINE_OPTIONS.MILLEAGE_BETWEEN_SERVICES.get(engine_type)
        current_milleage = self.LAST_ENGINE_SERVICE_MILLEAGE + milleage_between_services - 5
        last_time_battery_service = datetime.today() - timedelta(weeks=9999)
        return self.CAR_FACTORY.create(current_milleage, self.LAST_ENGINE_SERVICE_MILLEAGE, False, self.CURRENT_DATE,
                                       last_time_battery_service, engine_type, battery_type)

    def _create_car_with_huge_time_without_engine_service(self, engine_type: EngineType, battery_type: BatteryType) -> Car:
        milleage_between_services = self.ENGINE_OPTIONS.MILLEAGE_BETWEEN_SERVICES.get(engine_type)
        current_milleage = self.LAST_ENGINE_SERVICE_MILLEAGE + milleage_between_services - 5
        last_time_battery_service = datetime.today() - timedelta(weeks=9999)
        return self.CAR_FACTORY.create(current_milleage, self.LAST_ENGINE_SERVICE_MILLEAGE, False,
                                       last_time_battery_service, self.CURRENT_DATE, engine_type, battery_type)
