from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from core.apps.customers.services.codes import ICodeService
from core.apps.customers.services.customers import ICustomerService
from core.apps.customers.services.senders import ISenderService


# TODO выпилить бизнес логигу и перенести в use_cases


@dataclass(eq=False)
class IAuthService(ABC):
    customer_service: ICustomerService
    codes_service: ICodeService
    send_service: ISenderService

    @abstractmethod
    def authorize(self, phone: str): ...

    @abstractmethod
    def confirm(self, code: str, phone: str): ...


class AuthService(IAuthService):
    def authorize(self, phone: str):
        customer = self.customer_service.get_or_create(phone)
        code = self.codes_service.generate_code(customer)
        self.send_service.send_code(code, customer)

    def confirm(self, code: str, phone: str):
        customer = self.customer_service.get_by_phone(phone)
        self.codes_service.validate_code(code, customer)

        return self.customer_service.generate_token(customer)
