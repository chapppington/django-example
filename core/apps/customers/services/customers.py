from abc import (
    ABC,
    abstractmethod,
)
from uuid import uuid4

from core.apps.customers.entities.customers import CustomerEntity
from core.apps.customers.exceptions.customers import CustomerTokenInvalidException
from core.apps.customers.models import CustomerModel


class ICustomerService(ABC):
    @abstractmethod
    def get_or_create(self, phone: str) -> CustomerEntity: ...

    @abstractmethod
    def generate_token(self, customer: CustomerEntity) -> str: ...

    @abstractmethod
    def get_by_phone(self, phone: str) -> CustomerEntity: ...

    @abstractmethod
    def get_by_token(self, token: str) -> CustomerEntity: ...


class ORMCustomerService(ICustomerService):
    def get_or_create(self, phone: str) -> CustomerEntity:
        customer_dto, _ = CustomerModel.objects.get_or_create(phone=phone)

        return customer_dto.to_entity()

    def get_by_phone(self, phone: str) -> CustomerEntity:
        customer_dto = CustomerModel.objects.get(phone=phone)
        return customer_dto.to_entity()

    def generate_token(self, customer: CustomerEntity) -> str:
        new_token = str(uuid4())
        CustomerModel.objects.filter(phone=customer.phone).update(token=new_token)
        return new_token

    def get_by_token(self, token: str) -> CustomerEntity:
        try:
            customer_dto = CustomerModel.objects.get(token=token)
        except CustomerModel.DoesNotExist:
            raise CustomerTokenInvalidException(token=token)

        return customer_dto.to_entity()
