from abc import (
    ABC,
    abstractmethod,
)
from typing import Iterable

from django.db.models import Q

from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilters
from core.apps.products.entities.products import ProductEntity
from core.apps.products.exceptions.products import ProductNotFoundException
from core.apps.products.models import ProductModel


class IProductService(ABC):
    @abstractmethod
    def get_all(self) -> Iterable[ProductEntity]: ...

    @abstractmethod
    def get_by_id(self, product_id: int) -> ProductEntity: ...

    @abstractmethod
    def get_product_list(
        self,
        filters: ProductFilters,
        pagination: PaginationIn,
    ) -> Iterable[ProductEntity]: ...

    @abstractmethod
    def get_product_count(self, filters: ProductFilters) -> int: ...


class ORMProductService(IProductService):
    def _build_get_product_list_query(self, filters: ProductFilters) -> Q:
        query = Q(is_visible=True)

        if filters.search is not None:
            query &= Q(title__icontains=filters.search) | Q(
                description__icontains=filters.search,
            )

        return query

    def get_by_id(self, product_id: int) -> ProductEntity:
        try:
            product_dto = ProductModel.objects.get(id=product_id)
        except ProductModel.DoesNotExist:
            raise ProductNotFoundException(product_id=product_id)

        return product_dto.to_entity()

    def get_product_list(
        self,
        filters: ProductFilters,
        pagination: PaginationIn,
    ) -> Iterable[ProductEntity]:
        query = self._build_get_product_list_query(filters)

        queryset = ProductModel.objects.filter(query)[
            pagination.offset : pagination.offset + pagination.limit
        ]

        return [product.to_entity() for product in queryset]

    def get_product_count(self, filters: ProductFilters) -> int:
        query = self._build_get_product_list_query(filters)
        return ProductModel.objects.filter(query).count()

    def get_all(self) -> Iterable[ProductEntity]:
        query = self._build_get_product_list_query(ProductFilters())
        queryset = ProductModel.objects.filter(query)

        for product in queryset:
            yield product.to_entity()
