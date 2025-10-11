from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from core.apps.customers.entities.customers import CustomerEntity
from core.apps.products.entities.products import ProductEntity
from core.apps.products.entities.reviews import ReviewEntity
from core.apps.products.exceptions.reviews import ReviewInvalidRatingException
from core.apps.products.models import ReviewModel


class IReviewService(ABC):
    @abstractmethod
    def save_review(
        self,
        product: ProductEntity,
        customer: CustomerEntity,
        review: ReviewEntity,
    ) -> ReviewEntity: ...


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


class IReviewValidatorService(ABC):
    @abstractmethod
    def validate(
        self,
        review: ReviewEntity,
        *args,
        **kwargs,
    ): ...


class ReviewValidatorService(IReviewValidatorService):
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
class ComposedReviewValidatorService(IReviewValidatorService):
    validators: list[IReviewValidatorService]

    def validate(
        self,
        review: ReviewEntity,
        *args,
        **kwargs,
    ):
        for validator in self.validators:
            validator.validate(review, *args, **kwargs)
