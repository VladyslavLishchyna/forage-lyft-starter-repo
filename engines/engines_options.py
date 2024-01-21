from engines.engine_type import EngineType
from engines.service_needed_checkers.engine_service_needed_checking_type import EngineServiceNeededCheckingType


class EnginesOptions:
    MILLEAGE_BETWEEN_SERVICES = {
        EngineType.CAPULET: 30000,
        EngineType.WILLOUGHBY: 60000,
        EngineType.STERNMAN: 0,
    }

    TYPE_OF_ENGINE_SERVICE_NEEDED_CHECK = {
        EngineType.CAPULET: EngineServiceNeededCheckingType.BY_MILLEAGE,
        EngineType.WILLOUGHBY: EngineServiceNeededCheckingType.BY_MILLEAGE,
        EngineType.STERNMAN: EngineServiceNeededCheckingType.BY_INDICATOR,
    }
