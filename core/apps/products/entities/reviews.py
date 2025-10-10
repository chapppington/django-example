from dataclasses import (
    dataclass,
    field,
)

from core.apps.common.enums import EntityStatus
from core.apps.customers.entities.customers import CustomerEntity
from core.apps.products.entities.products import ProductEntity


@dataclass
class ReviewEntity:
    id: int
    product: ProductEntity | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    customer: CustomerEntity | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    rating: int = field(default=1)
    comment: str = field(default="")
