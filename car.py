from datetime import datetime
from abstract.serviceable import Serviceable
from batteries.battery import Battery
from engines.engine import Engine


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
