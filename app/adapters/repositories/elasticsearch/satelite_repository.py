from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from uuid import UUID
from typing import Dict, Any, List
from app.ports.telemetry_storage import TelemetryStoreService


class TelemetryStore(TelemetryStoreService):

    def __init__(self, host: str, port: int):
        url = f"{host}:{port}"
        self.client = Elasticsearch([url])

    def add(self, index: str, document: Dict[str, Any]) -> None:
        self.client.index(index=index, body=document)

    def add_bulk(self, index: str, documents: List[Dict[str, Any]]) -> None:
        actions = [{"_index": index, "_source": document} for document in documents]
        bulk(self.client, actions)

    def delete(self, index: str, document_id: UUID) -> None:
        self.client.delete(index=index, id=str(document_id))

    def update(self, index: str, document_id: UUID, document: Dict[str, Any]) -> None:
        self.client.update(index=index, id=str(document_id), body={"doc": document})
