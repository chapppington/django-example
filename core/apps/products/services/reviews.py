from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from core.apps.customers.entities.customers import CustomerEntity
from core.apps.products.entities.products import ProductEntity
from core.apps.products.entities.reviews import ReviewEntity
from core.apps.products.exceptions.reviews import (
    ReviewAlreadyExistsException,
    ReviewInvalidRatingException,
)
from core.apps.products.models import ReviewModel


class IReviewService(ABC):
    @abstractmethod
    def save_review(
        self,
        product: ProductEntity,
        customer: CustomerEntity,
        review: ReviewEntity,
    ) -> ReviewEntity: ...

    @abstractmethod
    def check_review_exists(
        self,
        product: ProductEntity,
        customer: CustomerEntity,
    ) -> bool: ...


class ORMReviewService(IReviewService):
    def save_review(
        self,
        product: ProductEntity,
        customer: CustomerEntity,
        review: ReviewEntity,
    ) -> ReviewEntity:
        review_dto = ReviewModel.from_entity(
            review=review,
            product=product,
            customer=customer,
        )
        review_dto.save()
        return review_dto.to_entity()

    def check_review_exists(
        self,
        product: ProductEntity,
        customer: CustomerEntity,
    ) -> bool:
        review_exists = ReviewModel.objects.filter(
            product_id=product.id,
            customer_id=customer.id,
        ).exists()
        return review_exists


class IReviewValidatorService(ABC):
    @abstractmethod
    def validate(
        self,
        review: ReviewEntity,
        *args,
        **kwargs,
    ): ...


class ReviewRatingValidatorService(IReviewValidatorService):
    def validate(
        self,
        review: ReviewEntity,
        *args,
        **kwargs,
    ):
        # TODO константы
        if not (1 <= review.rating <= 5):
            raise ReviewInvalidRatingException(rating=review.rating)


@dataclass
class SingleReviewValidatorService(IReviewValidatorService):
    review_service: IReviewService

    def validate(
        self,
        customer: CustomerEntity,
        product: ProductEntity,
        *args,
        **kwargs,
    ):
        review_exists = self.review_service.check_review_exists(
            product=product,
            customer=customer,
        )
        if review_exists:
            raise ReviewAlreadyExistsException(
                product_id=product.id,
                customer_id=customer.id,
            )


@dataclass
class ComposedReviewValidatorService(IReviewValidatorService):
    validators: list[IReviewValidatorService]

    def validate(
        self,
        review: ReviewEntity,
        customer: CustomerEntity,
        product: ProductEntity,
    ):
        for validator in self.validators:
            validator.validate(review=review, customer=customer, product=product)
