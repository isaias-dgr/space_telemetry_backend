from abc import ABC, abstractmethod
from typing import Dict, Any, List
from uuid import UUID


class SatelliteStoreService(ABC):
    @abstractmethod
    def add(self, document: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def delete(self, document_id: UUID) -> None:
        pass

    @abstractmethod
    def add_bulk(self, documents: List[Dict[str, Any]]) -> None:
        pass

    @abstractmethod
    def update(self, document_id: UUID, document: Dict[str, Any]) -> None:
        pass
