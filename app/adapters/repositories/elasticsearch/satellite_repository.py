from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from uuid import UUID
from typing import Dict, Any, List
from app.ports.satellite_storage import SatelliteStoreService
from app.adapters.repositories.elasticsearch.repository import ElasticStore


class SatelliteStore(
    ElasticStore,
    SatelliteStoreService,
):
    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        self.index = "satellites"

    def add(self, document: Dict[str, Any]) -> None:
        super().add(self.index, document)

    def add_bulk(self, documents: List[Dict[str, Any]]) -> None:
        super().add_bulk(self.index, documents)

    def get_dashboard(self) -> List[Dict[str, Any]]:
        raise NotImplementedError
