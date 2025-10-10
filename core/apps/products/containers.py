from dependency_injector import (
    containers,
    providers,
)

from core.apps.products.services.products import ORMProductService


class ProductContainer(containers.DeclarativeContainer):
    product_service = providers.Singleton(ORMProductService)
