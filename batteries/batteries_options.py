from datetime import timedelta
from batteries.battery import BatteryType

class BatteriesOptions():
    PERRIOD_BETWEEN_SERVICES = {
        BatteryType.NUBBIN: timedelta(days=365*4),
        BatteryType.SPINDLER: timedelta(days=365*2)
    }