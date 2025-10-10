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
from core.apps.customers.services.auth import IAuthService
from core.apps.products.containers import get_container


router = Router(tags=["customers"])


@router.post("auth", response=ApiResponse[AuthOutSchema], operation_id="authorize")
def authorize_handler(
    request: HttpRequest,
    schema: AuthInSchema,
) -> ApiResponse[AuthOutSchema]:
    container = get_container()
    service: IAuthService = container.resolve(IAuthService)

    service.authorize(schema.phone)

    return ApiResponse(
        data=AuthOutSchema(message=f"Code sent to phone {schema.phone}"),
    )


@router.post("confirm", response=ApiResponse[TokenOutSchema], operation_id="get_token")
def get_token_handler(
    request: HttpRequest,
    schema: TokenInSchema,
) -> ApiResponse[TokenOutSchema]:
    container = get_container()
    service: IAuthService = container.resolve(IAuthService)

    try:
        token = service.confirm(schema.code, schema.phone)
    except ServiceException as exception:
        raise HttpError(status_code=400, message=exception.message)

    return ApiResponse(
        data=TokenOutSchema(token=token),
    )
