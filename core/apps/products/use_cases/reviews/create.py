from dataclasses import dataclass

from core.apps.customers.services.customers import ICustomerService
from core.apps.products.entities.reviews import ReviewEntity
from core.apps.products.services.products import IProductService
from core.apps.products.services.reviews import (
    IReviewService,
    IReviewValidatorService,
)


@dataclass
class CreateReviewUseCase:
    review_service: IReviewService
    customer_service: ICustomerService
    product_service: IProductService
    validator_service: IReviewValidatorService

    def execute(
        self,
        product_id: int,
        customer_token: str,
        review: ReviewEntity,
    ) -> ReviewEntity:
        customer = self.customer_service.get_by_token(token=customer_token)
        product = self.product_service.get_by_id(product_id=product_id)

        self.validator_service.validate(
            review=review,
            customer=customer,
            product=product,
        )

        saved_review = self.review_service.save_review(
            product=product,
            customer=customer,
            review=review,
        )

        return saved_review
