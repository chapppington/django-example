from datetime import datetime

from ninja import Schema

from core.apps.products.entities.reviews import ReviewEntity


class ReviewInSchema(Schema):
    rating: int = 1
    comment: str = ""

    def to_entity(self) -> ReviewEntity:
        return ReviewEntity(
            rating=self.rating,
            comment=self.comment,
        )


class CreateReviewSchema(Schema):
    customer_token: str
    product_id: int
    review: ReviewInSchema


class ReviewOutSchema(ReviewInSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_entity(cls, review: ReviewEntity) -> "ReviewOutSchema":
        return cls(
            id=review.id,
            created_at=review.created_at,
            updated_at=review.updated_at,
            rating=review.rating,
            comment=review.comment,
        )
