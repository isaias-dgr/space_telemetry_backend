from app.domain.satellite import to_dict
from app.ports.space_service import SpaceXService
from app.ports.satellite_storage import SatelliteStoreService


class PollingSatellite:

    def __init__(
        self, space_service: SpaceXService, satellite_store: SatelliteStoreService
    ):
        self.space_service = space_service
        self.satellite_store = satellite_store

    def get_and_save_satellites(self):
        count = 0
        for satellite in self.space_service.get_satellites(page=1, limit=1000):
            self.satellite_store.add_bulk(to_dict(satellite))
            count += len(satellite)
        return count
