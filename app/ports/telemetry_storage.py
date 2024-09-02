from abc import ABC, abstractmethod
from typing import Dict, Any
from uuid import UUID


class TelemetryStoreService(ABC):
    @abstractmethod
    def add(self, index: str, document: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def delete(self, index: str, document_id: UUID) -> None:
        pass

    @abstractmethod
    def update(self, index: str, document_id: UUID, document: Dict[str, Any]) -> None:
        pass
