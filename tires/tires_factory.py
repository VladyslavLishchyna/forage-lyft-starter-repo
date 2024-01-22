from datetime import datetime
from typing import List

from tires.service_needed_checkers.implementations.tires_service_needed_checker_by_single_tire_wear import \
    TiresServiceNeededCheckerBySingleTireWear
from tires.service_needed_checkers.implementations.tires_service_needed_checker_by_total_tires_wear import \
    TiresServiceNeededCheckerByTotalTiresWear
from tires.service_needed_checkers.tires_service_needed_checking_type import TiresServiceNeededCheckingType
from tires.tires import Tires
from tires.tires_options import TiresOptions
from tires.tires_type import TiresType


class TiresFactory:
    TIRES_SERVICE_NEEDED_CHECKER_BY_SINGLE_TIRE_WEAR = TiresServiceNeededCheckerBySingleTireWear()
    TIRES_SERVICE_NEEDED_CHECKER_BY_TOTAL_TIRES_WEAR = TiresServiceNeededCheckerByTotalTiresWear()

    def __init__(self, tires_options: TiresOptions):
        self.tires_options = tires_options

    def create(self, last_service_date: datetime, tires_wear: List, tires_type: TiresType):
        service_needed_checker = self.__resolve_tires_service_needed_checker(tires_type)
        return Tires(last_service_date, tires_wear, service_needed_checker)

    def __resolve_tires_service_needed_checker(self, tires_type: TiresType):
        service_needed_checker_type = self.tires_options.TYPE_OF_TIRES_SERVICE_NEEDED_CHECK[tires_type]
        match service_needed_checker_type:
            case TiresServiceNeededCheckingType.BY_SINGLE_TIRE_WEAR:
                return self.TIRES_SERVICE_NEEDED_CHECKER_BY_SINGLE_TIRE_WEAR
            case TiresServiceNeededCheckingType.BY_TOTAL_TIRES_WEAR:
                return self.TIRES_SERVICE_NEEDED_CHECKER_BY_TOTAL_TIRES_WEAR
            case _:
                raise 'Can`t resolve AbstractTiresServiceNeededChecker'
