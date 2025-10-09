"""
Test products service

1. Test products count zero, product count with existing products
2. Test product returns all/paginated products, filters (desc, title, no matches)
"""

import pytest
from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilters
from core.apps.products.services.products import IProductService
from tests.factories.products import ProductModelFactory


@pytest.mark.django_db
def test_get_products_count_zero(product_service: IProductService):
    """
    Test products count zero with no products
    """
    products_count = product_service.get_product_count(ProductFilters())
    assert products_count == 0, f"{products_count=}"


@pytest.mark.django_db
def test_get_products_count_existing_products(product_service: IProductService):
    """
    Test products count with existing products
    """
    expected_count = 5
    ProductModelFactory.create_batch(size=expected_count)

    products_count = product_service.get_product_count(ProductFilters())
    assert products_count == expected_count, f"{products_count=}"


@pytest.mark.django_db
def test_get_products_all(product_service: IProductService):
    expected_count = 5
    products = ProductModelFactory.create_batch(size=expected_count)

    products_titles = {product.title for product in products}

    fetched_products = product_service.get_product_list(ProductFilters(), PaginationIn())
    
    fetched_products_titles = {product.title for product in fetched_products}
    
    assert len(fetched_products_titles) == expected_count, f"{fetched_products_titles=}"
    assert fetched_products_titles == products_titles, f"{fetched_products_titles=}"