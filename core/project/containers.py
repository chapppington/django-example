from functools import lru_cache

from django.conf import settings

import punq
from httpx import Client

from core.apps.common.clients.elasticsearch import ElasticClient
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
from core.apps.products.services.reviews import (
    ComposedReviewValidatorService,
    IReviewService,
    IReviewValidatorService,
    ORMReviewService,
    ReviewRatingValidatorService,
    SingleReviewValidatorService,
)
from core.apps.products.services.search import (
    ElasticsearchSearchService,
    ISearchService,
)
from core.apps.products.use_cases.reviews.create import CreateReviewUseCase
from core.apps.products.use_cases.search.upsert_search_data import (
    UpsertSearchDataUseCase,
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
    container.register(IReviewService, ORMReviewService)

    container.register(SingleReviewValidatorService)
    container.register(ReviewRatingValidatorService)

    # init search service
    def build_validators() -> IReviewValidatorService:
        return ComposedReviewValidatorService(
            validators=[
                container.resolve(SingleReviewValidatorService),
                container.resolve(ReviewRatingValidatorService),
            ],
        )

    def build_elastic_search_service() -> ISearchService:
        return ElasticsearchSearchService(
            client=ElasticClient(http_client=Client(base_url=settings.ELASTIC_URL)),
            index_name=settings.ELASTIC_PRODUCT_INDEX,
        )

    container.register(
        service=IReviewValidatorService,
        factory=build_validators,
    )

    container.register(ISearchService, factory=build_elastic_search_service)

    container.register(CreateReviewUseCase)
    container.register(UpsertSearchDataUseCase)

    return container
