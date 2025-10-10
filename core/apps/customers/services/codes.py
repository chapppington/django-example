import random
from abc import (
    ABC,
    abstractmethod,
)

from django.core.cache import cache

from core.apps.customers.entities.customers import CustomerEntity
from core.apps.customers.exceptions.codes import (
    CodeNotFoundException,
    CodesNotEqualException,
)


class ICodeService(ABC):
    @abstractmethod
    def generate_code(self, customer: CustomerEntity) -> str: ...

    @abstractmethod
    def validate_code(self, code: str, customer: CustomerEntity) -> None: ...


class DjangoCacheCodeService(ICodeService):
    def generate_code(self, customer: CustomerEntity) -> str:
        code = str(random.randint(1000, 9999))
        cache.set(customer.phone, code)
        return code

    def validate_code(self, code: str, customer: CustomerEntity) -> None:
        cached_code = cache.get(customer.phone)

        if cached_code is None:
            raise CodeNotFoundException(code=code)

        if code != cached_code:
            raise CodesNotEqualException(
                code=code,
                cached_code=cached_code,
                customer_phone=customer.phone,
            )

        cache.delete(customer.phone)
