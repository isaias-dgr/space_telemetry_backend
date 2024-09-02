from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.launches import Launch


class LaunchRepository(ABC):
    @abstractmethod
    def create(self, name: str, description: str) -> Launch:
        pass

    @abstractmethod
    def get(self, launch_id: int) -> Optional[Launch]:
        pass

    @abstractmethod
    def get_alls(self) -> List[Launch]:
        pass

    @abstractmethod
    def update(self, launch_id: int, name: str, description: str) -> Optional[Launch]:
        pass

    @abstractmethod
    def delete(self, launch_id: int) -> bool:
        pass
