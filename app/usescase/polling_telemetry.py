from app.domain.launches import Launch
from app.domain.rockets import Rocket
from app.domain.satellite import Satellite
from app.ports.space_service import SpaceXService
from app.ports.telemetry_storage import TelemetryStoreService


class PollingTelemetry:
    # def __init__(
    #     self, space_service: SpaceXService, telemetry_store: TelemetryStoreService
    # ):
    #     self.space_service = space_service
    #     self.telemetry_store = telemetry_store

    def get_and_save_launches(self):
        return "PollingTelemetry"
