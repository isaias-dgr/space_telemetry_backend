from app.ports.space_service import SpaceXService
from app.ports.rockets_storage import RocketRepository


class PollingRocket:

    def __init__(self, space_service: SpaceXService, rocket_store: RocketRepository):
        self.space_service = space_service
        self.rocket_store = rocket_store

    def get_and_save_rockets(self):
        count = 0
        for rocket in self.space_service.get_rockets(page=1, limit=1000):
            self.rocket_store.add(rocket)
            count += 1
        return count
