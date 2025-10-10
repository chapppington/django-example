from abc import (
    ABC,
    abstractmethod,
)

from core.apps.customers.entities.customers import CustomerEntity


class ISenderService(ABC):
    @abstractmethod
    def send_code(self, code: str, customer: CustomerEntity) -> None: ...


class DummySendService(ISenderService):
    def send_code(self, code: str, customer: CustomerEntity) -> None:
        print(f"Sending code {code} to customer {customer.phone}")
