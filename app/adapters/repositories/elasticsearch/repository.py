from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from uuid import UUID
from typing import Dict, Any, List


class ElasticStore:
    def __init__(self, host: str, port: int):
        url = f"{host}:{port}"
        self.client = Elasticsearch([url])

    def add(self, index: str, document: Dict[str, Any]) -> None:
        self.client.index(index=index, body=document)

    def add_bulk(self, index: str, documents: List[Dict[str, Any]]) -> None:
        actions = [{"_index": index, "_source": document} for document in documents]
        bulk(self.client, actions)

    def get_query(self, index: str, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        response = self.client.search(index=index, body=query)
        return response["aggregations"]