from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class ProductException(ServiceException):
    @property
    def message(self) -> str:
        return "Product exception occurred"


@dataclass(eq=False)
class ProductNotFoundException(ProductException):
    product_id: int

    @property
    def message(self) -> str:
        return f"Product not found with id {self.product_id}"
