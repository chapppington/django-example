from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class CustomerException(ServiceException):
    @property
    def message(self) -> str:
        return "Customer exception occurred"


@dataclass(eq=False)
class CustomerTokenInvalidException(CustomerException):
    token: str

    @property
    def message(self) -> str:
        return "Customer token is invalid"
