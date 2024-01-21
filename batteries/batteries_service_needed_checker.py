from datetime import timedelta
from datetime import datetime


class BatteriesServiceNeededChecker:
    def __init__(self, time_between_services: timedelta):
        self.time_between_services = time_between_services

    def needs_service(self, last_service_date: datetime) -> bool:
        next_service_date = last_service_date + self.time_between_services
        return next_service_date < datetime.today()
