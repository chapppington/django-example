from abc import ABC, abstractmethod
from typing import Iterable

from django.db.models import Q

from core.apps.products.entities.products import ProductEntity
from core.apps.products.models import ProductModel
from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilters


class IProductService(ABC):
    @abstractmethod
    def get_product_list(self) -> Iterable[ProductEntity]: ...

    @abstractmethod
    def get_product_count(self) -> int: ...


# TODO закинуть фильтры в сервисный слой чтобы избежать нарушения принципа инверсии зависимостей
class ORMProductService(IProductService):
    def _build_get_product_list_query(self, filters: ProductFilters) -> Q:
        query = Q(is_visible=True)

        if filters.search is not None:
            query &= Q(title__icontains=filters.search) | Q(
                description__icontains=filters.search
            )

        return query

    def get_product_list(
        self, filters: ProductFilters, pagination: PaginationIn
    ) -> Iterable[ProductEntity]:
        query = self._build_get_product_list_query(filters)

        queryset = ProductModel.objects.filter(query)[
            pagination.offset : pagination.offset + pagination.limit
        ]

        return [product.to_entity() for product in queryset]

    def get_product_count(self, filters: ProductFilters) -> int:
        query = self._build_get_product_list_query(filters)
        return ProductModel.objects.filter(query).count()
