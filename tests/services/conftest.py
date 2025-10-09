import pytest

from core.apps.products.services.products import (
    IProductService,
    ORMProductService,
)


@pytest.fixture
def product_service() -> IProductService:
    return ORMProductService()
