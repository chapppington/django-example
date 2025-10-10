from functools import lru_cache

import punq

from core.apps.customers.services.auth import (
    AuthService,
    IAuthService,
)
from core.apps.customers.services.codes import (
    DjangoCacheCodeService,
    ICodeService,
)
from core.apps.customers.services.customers import (
    ICustomerService,
    ORMCustomerService,
)
from core.apps.customers.services.senders import (
    ComposeSenderService,
    EmailSenderService,
    ISenderService,
    PushSenderService,
)
from core.apps.products.services.products import (
    IProductService,
    ORMProductService,
)


@lru_cache(maxsize=1)
def get_container() -> punq.Container:
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()
    # init product service
    container.register(IProductService, ORMProductService)
    # init customer service
    container.register(ICustomerService, ORMCustomerService)

    # init code service
    container.register(ICodeService, DjangoCacheCodeService)

    # init sender service
    container.register(
        ISenderService,
        ComposeSenderService,
        sender_services=(
            EmailSenderService(),
            PushSenderService(),
        ),
    )

    # init auth service
    container.register(IAuthService, AuthService)

    return container
