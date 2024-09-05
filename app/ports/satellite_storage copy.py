from abc import ABC, abstractmethod
from typing import Dict, Any, List
from uuid import UUID


class SatelliteStoreService(ABC):
    @abstractmethod
    def add(self, index: str, document: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def delete(self, index: str, document_id: UUID) -> None:
        pass

    @abstractmethod
    def add_bulk(self, index: str, documents: List[Dict[str, Any]]) -> None:
        pass

    @abstractmethod
    def update(self, index: str, document_id: UUID, document: Dict[str, Any]) -> None:
        pass
