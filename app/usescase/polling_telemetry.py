from app.ports.space_service import SpaceXService
from app.ports.telemetry_storage import TelemetryStoreService


class PollingTelemetry:

    def __init__(
        self, space_service: SpaceXService, telemetry_store: TelemetryStoreService
    ):
        self.space_service = space_service
        self.telemetry_store = telemetry_store

    def get_and_save_launches(self):
        count = 0
        for launch in self.space_service.get_launches(page=1, limit=210):
            self.telemetry_store.add(launch.to_dict())
            count += 1
        return count
