from abc import ABC, abstractmethod
from typing import Dict, Any, List
from uuid import UUID


class SatelliteStoreService(ABC):
    @abstractmethod
    def add(self, document: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def add_bulk(self, documents: List[Dict[str, Any]]) -> None:
        pass

    @abstractmethod
    def get_dashboard(self) -> List[Dict[str, Any]]:
        pass