from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.rockets import Rocket


class RocketRepository(ABC):
    @abstractmethod
    def add(self, Rocket) -> Rocket:
        pass

    @abstractmethod
    def get(self, rocket_id: int) -> Optional[Rocket]:
        pass

    @abstractmethod
    def update(self, rocket_id: int, name: str, description: str) -> Optional[Rocket]:
        pass

    @abstractmethod
    def delete(self, rocket_id: int) -> bool:
        pass
