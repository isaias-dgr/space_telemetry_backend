from abc import ABC, abstractmethod
from typing import List

from app.domain.launches import Launch
from app.domain.rockets import Rocket
from app.domain.satellite import Satellite


class SpaceXService(ABC):
    @abstractmethod
    def get_launches(self) -> List[Launch]:
        pass

    @abstractmethod
    def get_rockets(self) -> List[Rocket]:
        pass

    @abstractmethod
    def get_satellites(self) -> List[Satellite]:
        pass
