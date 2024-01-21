from datetime import timedelta
from batteries.battery_type import BatteryType


class BatteriesOptions:
    TIME_BETWEEN_SERVICES = {
        BatteryType.NUBBIN: timedelta(days=365 * 4),
        BatteryType.SPINDLER: timedelta(days=365 * 2)
    }
