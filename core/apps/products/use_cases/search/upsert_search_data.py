from dataclasses import dataclass

from core.apps.products.services.products import IProductService
from core.apps.products.services.search import ISearchService


@dataclass
class UpsertSearchDataUseCase:
    search_service: ISearchService
    product_service: IProductService

    def execute(self):
        products = self.product_service.get_all()

        for product in products:
            self.search_service.upsert_product(product)
