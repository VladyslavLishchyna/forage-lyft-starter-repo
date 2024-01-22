from tires.service_needed_checkers.tires_service_needed_checking_type import TiresServiceNeededCheckingType
from tires.tires_type import TiresType


class TiresOptions:
    TYPE_OF_TIRES_SERVICE_NEEDED_CHECK = {
        TiresType.CARRIGAN: TiresServiceNeededCheckingType.BY_SINGLE_TIRE_WEAR,
        TiresType.OCTOPRIME: TiresServiceNeededCheckingType.BY_TOTAL_TIRES_WEAR,
    }
