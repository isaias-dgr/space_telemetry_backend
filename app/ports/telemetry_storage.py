from abc import ABC, abstractmethod
from typing import Dict, Any, List
from uuid import UUID

from app.domain.dashboard import Dashboard


class TelemetryStoreService(ABC):
    @abstractmethod
    def add(self, document: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def add_bulk(self, documents: List[Dict[str, Any]]) -> None:
        pass

    @abstractmethod
    def get_dashboard(self) -> Dashboard:
        pass