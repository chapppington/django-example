from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import Iterable

from core.apps.customers.entities.customers import CustomerEntity


class ISenderService(ABC):
    @abstractmethod
    def send_code(self, code: str, customer: CustomerEntity) -> None: ...


class DummySendService(ISenderService):
    def send_code(self, code: str, customer: CustomerEntity) -> None:
        print(f"Sending code {code} to customer {customer.phone}")


class EmailSenderService(ISenderService):
    def send_code(self, code: str, customer: CustomerEntity) -> None:
        print(f"Sending email to customer with code {code}")


class PushSenderService(ISenderService):
    def send_code(self, code: str, customer: CustomerEntity) -> None:
        print(f"Sending push to customer with code {code}")


@dataclass
class ComposeSenderService(ISenderService):
    sender_services: Iterable[ISenderService]

    def send_code(self, code: str, customer: CustomerEntity) -> None:
        for sender in self.sender_services:
            sender.send_code(code, customer)
