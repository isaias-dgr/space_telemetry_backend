from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.satellite import Satellite


class SatelliteRepository(ABC):
    @abstractmethod
    def create(self, name: str, description: str) -> Satellite:
        pass

    @abstractmethod
    def get(self, satellite_id: int) -> Optional[Satellite]:
        pass

    @abstractmethod
    def get_alls(self) -> List[Satellite]:
        pass

    @abstractmethod
    def update(
        self, satellite_id: int, name: str, description: str
    ) -> Optional[Satellite]:
        pass

    @abstractmethod
    def delete(self, satellite_id: int) -> bool:
        pass
