from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from core.apps.common.clients.elasticsearch import ElasticClient
from core.apps.products.entities.products import ProductEntity


@dataclass
class ISearchService(ABC):
    @abstractmethod
    def upsert_product(self, product: ProductEntity): ...


@dataclass
class ElasticsearchSearchService(ISearchService):
    client: ElasticClient
    index_name: str

    def upsert_product(self, product: ProductEntity):
        self.client.upsert_index(
            index=self.index_name,
            document_id=product.id,
            document={
                "title": product.title,
                "description": product.description,
                "tags": product.tags,
            },
        )
