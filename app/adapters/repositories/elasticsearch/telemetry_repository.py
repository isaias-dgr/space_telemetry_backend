from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from uuid import UUID
from typing import Dict, Any, List
from app.adapters.repositories.elasticsearch.repository import ElasticStore
from app.ports.telemetry_storage import TelemetryStoreService


class TelemetryStore(
    ElasticStore,
    TelemetryStoreService,
):

    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        self.index = "telemetry"

    def add(self, document: Dict[str, Any]) -> None:
        super().add(self.index, document)

    def add_bulk(self, documents: List[Dict[str, Any]]) -> None:
        super().add_bulk(self.index, documents)

    def delete(self, document_id: UUID) -> None:
        super().delete(self.index, document_id)

    def update(self, document_id: UUID, document: Dict[str, Any]) -> None:
        super().update(self.index, document_id, document)
