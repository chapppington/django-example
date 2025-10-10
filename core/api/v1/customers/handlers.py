from django.http import HttpRequest
from ninja import Router
from ninja.errors import HttpError

from core.api.schemas import ApiResponse
from core.api.v1.customers.schemas import (
    AuthInSchema,
    AuthOutSchema,
    TokenInSchema,
    TokenOutSchema,
)
from core.apps.common.exceptions import ServiceException
from core.apps.customers.services.auth import (
    AuthService,
    IAuthService,
)
from core.apps.customers.services.codes import DjangoCacheCodeService
from core.apps.customers.services.customers import ORMCustomerService
from core.apps.customers.services.senders import DummySendService


router = Router(tags=["customers"])


@router.post("auth", response=ApiResponse[AuthOutSchema], operation_id="authorize")
def authorize_handler(
    request: HttpRequest,
    schema: AuthInSchema,
) -> ApiResponse[AuthOutSchema]:
    service: IAuthService = AuthService(
        customer_service=ORMCustomerService(),
        codes_service=DjangoCacheCodeService(),
        send_service=DummySendService(),
    )

    service.authorize(schema.phone)

    return ApiResponse(
        data=AuthOutSchema(message=f"Code sent to phone {schema.phone}"),
    )


@router.post("confirm", response=ApiResponse[TokenOutSchema], operation_id="get_token")
def get_token_handler(
    request: HttpRequest,
    schema: TokenInSchema,
) -> ApiResponse[TokenOutSchema]:
    service: IAuthService = AuthService(
        customer_service=ORMCustomerService(),
        codes_service=DjangoCacheCodeService(),
        send_service=DummySendService(),
    )

    try:
        token = service.confirm(schema.code, schema.phone)
    except ServiceException as exception:
        raise HttpError(status_code=400, message=exception.message)

    return ApiResponse(
        data=TokenOutSchema(token=token),
    )
