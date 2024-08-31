from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from typing import Dict, Any
from uuid import UUID
from app.ports.telemetry import TelemetryStoreService


class TelemetryStore(TelemetryStoreService):
    def __init__(self, host: str, port: int):
        self.client = Elasticsearch(host=host, port=port)

    def add(self, index: str, document: Dict[str, Any]) -> None:
        self.client.index(index=index, body=document)

    def delete(self, index: str, document_id: UUID) -> None:
        self.client.delete(index=index, id=str(document_id))

    def update(self, index: str, document_id: UUID, document: Dict[str, Any]) -> None:
        self.client.update(index=index, id=str(document_id), body={"doc": document})
