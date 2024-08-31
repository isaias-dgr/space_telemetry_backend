from abc import ABC, abstractmethod


class SpaceXService(ABC):
    @abstractmethod
    def get_launches(self) -> List[Launch]:
        pass

    @abstractmethod
    def get_rockets(self) -> List[Rocket]:
        pass

    @abstractmethod
    def get_starlink(self) -> List[Satellite]:
        pass
